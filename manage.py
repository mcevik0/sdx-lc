""" flask manage """
from flask.cli import FlaskGroup

from swagger_server import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
