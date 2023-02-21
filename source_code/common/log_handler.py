import logging
import os
import sys
from  datetime import datetime

class AppLogHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__(stream=sys.stdout)
        logging.Handler.__init__(self)


'''
--------------DOC---------------------

The code defines a custom logging handler called AppLogHandler.

The handler extends the built-in logging.StreamHandler class and overrides its constructor. The constructor initializes
 the handler by calling the constructor of the parent class and passing sys.stdout as the stream to write logs to.

This handler can be used to send log messages to standard output (i.e. the console), as opposed to writing them to a 
file or sending them to a remote log server.


'''