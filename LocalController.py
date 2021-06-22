from MessageQueue import *
from optparse import OptionParser
import argparse
import sqlite3
from sqlite3 import Error
import dataset

class LocalController():
    ''' This is the main coordinating module of the local controller. It mostly 
        provides startup and coordination, rather than performan many actions by
        itself.
        Singleton. ''' 

    def __init__(self, options=None):
        ''' The bulk of the work happens here. This initializes nearly 
            everything and starts up the main processing loop for the entire SDX
            Controller. '''
        self.loggerid = 'localcontroller'
        self.logfilename = 'localcontroller.log'
        self.debuglogfilename = None

        manifest = options.manifest
        db = options.dbfile

        #run_topo = options.topo

        serverconfigure = RabbitmqConfigure(queue='hello',
                               host='localhost',
                               routingKey='hello',
                               exchange='')

        rabbitmq = RabbitMq(serverconfigure)
        # Testing message
        rabbitmq.publish(body={"localctlr":1})
        # response = rabbitmq.call()
        # print(" [.] Got %r" % response)
        


    def _initialize_db(self, db_filename, db_tables_tuples,
                        print_table_on_load=False):
        # A lot of modules will need DB access for storing data, but some use a
        # DB for storing configuration information as well. This is *optional*
        # to use, which is why it's not part of __init__()
        # Details on the setup:
        # https://dataset.readthedocs.io/en/latest/api.html
        # https://github.com/g2p/bedup/issues/38#issuecomment-43703630
        self.logger.critical("Connection to DB: %s" % db_filename)
        self.db = dataset.connect('sqlite:///' + db_filename, 
                                    engine_kwargs={'connect_args':
                                                    {'check_same_thread':False}})

        #Try loading the tables, if they don't exist, create them.
        for (name, table) in db_tables_tuples:
            if table in self.db: #https://github.com/pudo/dataset/issues/281
                self.logger.info("Trying to load %s from DB" % name)
                t = self.db.load_table(table)
                if print_table_on_load:
                    entries = t.find()
                    #print "\n\n&&&&& ENTRIES in %s &&&&&" % name
                    for e in entries:
                        print ("\n%s" % str(e))
                    #print "&&&&& END ENTRIES &&&&&\n\n"
                    
                setattr(self, name, t)
                
            else:
                # If load_table() fails, that's fine! It means that the
                # table doesn't yet exist. So, create it.
                self.logger.info("Failed to load %s from DB, creating table" %
                                    name)
                t = self.db[table]
                setattr(self, name, t)
    
    
if __name__ == '__main__':
    parser = OptionParser()

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-d", "--dbfile", dest="dbfile", type=str, 
                        action="store", help="Specifies the database ", 
                        default=":memory:")
    
    parser.add_argument("-m", "--manifest", dest="manifest", type=str, 
                        action="store", help="specifies the manifest")
    #
    # parser.add_argument("-N", "--no_topo", dest="topo", default=True, 
    #                     action="store_false", help="Run without the topology")
    #
    # parser.add_argument("-H", "--host", dest="host", default='0.0.0.0', 
    #                     action="store", type=str, help="Choose a host address ")
    #
    # parser.add_argument("-p", "--port", dest="port", default=5000, 
    #                     action="store", type=int, 
    #                     help="Port number of web interface")
    #
    # parser.add_argument("-e", "--sense", dest="sport", default=5001, 
    #                     action="store", type=int, 
    #                     help="Port number of SENSE interface")

    #parser.add_argument("-l", "--lcport", dest="lcport", default=PORT,
    #                    action="store", type=int,
    #                    help="Port number for LCs to connect to")

    # Failure handling, enabled by default
    #parser.add_argument("-f", "--failrecover", dest="failrecover", default=True,
    #                    action="store_false", help="Run with failure recover")

    options = parser.parse_args()

    if not options.manifest:
        parser.print_help()
        exit()
        
    lc = LocalController(options)