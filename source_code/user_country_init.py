import os
import logging
from logging.config import dictConfig
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) , 'common'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) , 'source_code'))
from log_config.logconfig import log_config
from flask.logging import default_handler
import source_code
def manageApp():
    """ Handles app startup.

    Args:

    Returns:
        app object
    """
    load_dotenv(override=True)
    app = Flask(__name__)

    dictConfig(log_config)


    app.logger.removeHandler(default_handler)

    # configuring routes
    source_code.customer_details_verification_init(app)
    CORS(app,allow_headers='authorization_key,content-type', origins='*')

    # main app log
    logger = logging.getLogger('main_app')


    logger.info('******************Started App*******************')
    return app

'''--------DOC-----------------
The code defines a function called manageApp(), which is responsible for setting up a Flask application.

Firstly, the function loads the environment variables from a .env file using load_dotenv(). Then, a new Flask app object is created using the Flask() constructor.

Next, the app's logging configuration is set up by loading the logging configuration from log_config file using the dictConfig() method from logging.config.

The default logging handler for Flask is removed from the app's logger by calling removeHandler() method on the app's logger. 
This is done to avoid logs being duplicated.

Then, the application routes are configured by calling the customer_details_verification_init() function from source_code module,
 which registers blueprints with the app object. CORS is also enabled to allow cross-origin resource sharing.

Finally, the logger is obtained and a log message is printed to indicate that the app has started. The app object is then returned by the function.


'''