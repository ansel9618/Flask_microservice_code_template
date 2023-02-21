log_config={
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }


'''
The above code is a configuration for the Python logging module. It defines a dictionary with several keys and values:

version: The version of the logging configuration file format.
formatters: A dictionary containing one or more named formatter configurations. In this case, there is only one named 
'default', which specifies the log message format to use.
handlers: A dictionary containing one or more named handler configurations. In this case, there is only one named 'wsgi', 
which specifies the log output stream and formatter to use.

root: A dictionary containing configuration for the root logger. This logger is the parent of all loggers, and any log
 message not captured by a more specific logger will be handled by this one. In this case, the logger level is set to INFO, 
 meaning that log messages with a severity level of INFO or higher will be captured, and the 'wsgi' handler will be used to output log messages.

'''