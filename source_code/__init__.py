import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'common'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'country_details'))
from sqlalchemy import create_engine,Table, MetaData
from dotenv import load_dotenv
load_dotenv(override=True)
from log_config.log_data import ApplicationLogger as applog

from country_details.ms_get_countries import bp_get_country

DB_DRIVER = os.getenv('DBDRIVER')
SCHEMA = os.getenv('SCHEMA')
POOL_SIZE = os.getenv('POOL_SIZE')
DB_USER = os.getenv('DBUSER')
DB_PASS = os.getenv('DBPASS')
DB_HOST = os.getenv('DBHOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DBNAME')

def customer_details_verification_init(app):
    app.register_blueprint(bp_get_country, url_prefix='/onboarding/list-stages/')

    update_from_db(app)

def update_from_db(app):
    applog.info("inside update_from_db fn:")
    try:
        if 'engine' not in app.config:
            app.config['engine'] = create_enginee(applog, app)
    except Exception as exp:
        applog.debug("Exception occurred while updating app log_config " + str(exp))


def create_enginee(applog,app):
    applog.info("Starting to create engine")
    engine = None
    try:

        sql_client_driver = DB_DRIVER
        connection_string = sql_client_driver \
                            + DB_USER \
                            + ":" + DB_PASS \
                            + "@" + DB_HOST \
                            + "/" + DB_NAME
        engine = create_engine(connection_string, pool_size=20,
                               connect_args={'options': '-csearch_path={}'.format(str(SCHEMA))})


        if "customer" not in app.config:
            mst_application_stage(app, applog, engine)

        connec = engine.connect()
        connec.close()
        applog.info("Finished creating connection")
    except Exception as exp:
        applog.debug("Exception occurred while updating app log_config " + str(exp))
    finally:
        return engine

def mst_application_stage(app,applog,engine):
    applog.info("Starting to create mst_application_stage")
    mst_application_stage = None
    try:
        mst_application_stage = Table("country_table", MetaData(), autoload_with=engine)

    except Exception as exp:
        applog.debug("Exception occurred while mst_application_stage table " + str(exp))
    finally:
        app.config['country_table'] = mst_application_stage

'''
--------------DOC-----------------

The above code is a Python module that initializes a Flask application with some configuration parameters, registers a Flask blueprint, and creates a database connection engine using SQLAlchemy.

Let's break down the code step by step:

First, the module imports several modules including sys, os, sqlalchemy, dotenv, and a custom ApplicationLogger class for logging.
Next, the module sets up the database connection parameters by loading them from environment variables using the dotenv.load_dotenv() function.

Then, the module defines a function called customer_details_verification_init that takes in the Flask app object as an argument. 
This function registers a Flask blueprint and calls the update_from_db function to create the database connection engine.

The update_from_db function is responsible for creating the database engine if it does not already exist in the Flask app config. 
If it does exist, then it does nothing. It calls the create_enginee function to create the engine.

The create_enginee function creates a database engine using the sqlalchemy.create_engine() function. It also sets the 
database schema and pool size using the global SCHEMA and POOL_SIZE variables defined earlier. It then creates a Table object 
for the country_table table using the sqlalchemy.Table() function and assigns it to the Flask app config as app.config['country_table'].

Finally, the mst_application_stage function is responsible for loading the country_table table into the Flask app config as a SQLAlchemy 
Table object using the sqlalchemy.Table() function. If there is an error, it logs the error message.

Overall, this module sets up a Flask application with a database connection engine using SQLAlchemy, defines a blueprint for handling 
HTTP requests, and loads a database table into the Flask app config for use in other parts of the application.

'''
