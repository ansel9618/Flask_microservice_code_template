import os
import sys
from sqlalchemy.orm import Session
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'common'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'third_party_api'))
from app_response import AppResponse
from utilities import Utils
from sqlalchemy import create_engine, Table, MetaData
from source_code.country_messages.Cmessages import Messages
from flask import current_app as cp
from log_config.log_data import ApplicationLogger as applog
from dotenv import load_dotenv
load_dotenv(override=True)

DB_DRIVER = os.getenv('DBDRIVER')
SCHEMA = os.getenv('SCHEMA')
POOL_SIZE = os.getenv('POOL_SIZE')
DB_USER = os.getenv('DBUSER')
DB_PASS = os.getenv('DBPASS')
DB_HOST = os.getenv('DBHOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DBNAME')

class Country_details:
    def __init__(self, logger):
        if logger:
            self.logger = logger
        else:
            self.logger = applog

        self.sqlHandlerObj = None

    def __enter__(self):
        class SqlQueryHandler:
            def __init__(self, logger):
                if logger:
                    self.logger = logger
                else:
                    self.logger = applog

                sql_client_driver = DB_DRIVER
                connection_string = sql_client_driver\
                                    + DB_USER\
                                    +":"+DB_PASS\
                                    +"@"+DB_HOST\
                                    +"/"+DB_NAME

                self.session = None
                self.connection = None
                self.engine = None
                if "engine" in cp.config and cp.config['engine'] is not None:
                    self.engine = cp.config['engine']
                else:
                    self.engine = create_engine(connection_string, pool_size=20,
                                                connect_args={'options': '-csearch_path={}'.format(str(SCHEMA))})
                    cp.config["engine"] = self.engine
                self.connection = self.engine.connect()
                self.app_response = AppResponse()


            def get_country(self):
                """
                Making connection with database and getting the country table details,
                Returns: Response (code, data, message, status)
                data: id,code,description
                """
                resp = AppResponse()
                try:
                    self.logger.info("inside get_country")
                    self.session = Session(self.connection)
                    if "country_table" in cp.config and cp.config["country_table"] is not None:
                        mst_country = cp.config["country_table"]
                    else:
                        mst_country = Table("country_table", MetaData(), autoload_with=self.engine)
                        cp.config["country_table"] = mst_country
                    application_stage = self.session \
                        .query(mst_country) \
                        .limit(10)
                    mst_country_list= []

                    if application_stage:
                        for item in application_stage:
                            obj = {"Code":item.country_code,"Country_Name": item.country_name}
                            mst_country_list.append(obj)

                        self.session.commit()
                        self.session.close()
                        resp.set_response(200, sorted(mst_country_list, key=lambda x: x["Code"]), Messages.COUNTRY_LIST_SUCCESS,\
                                          Messages.TRUE)
                    else:
                        self.logger.info("No country list available ")
                        resp.set_response(500, {}, Messages.STAGE_LIST_FAILED,\
                                          Messages.FALSE)

                except Exception as excp:
                    Utils.process_exception(excp, self.logger,
                                            f'{Messages.INTERNAL_ERROR}during getting country list', resp)
                finally:
                    self.logger.info("get_country function completed")
                    return resp

            def cleanup(self):
                self.logger.info("Going to do DB cleanup")
                try:
                    if self.session is not None:
                        self.session.close()
                    if self.connection is not None:
                        self.connection.close()
                except Exception as exp:
                    Utils.process_exception(exp, self.logger, 'Exception occurred during get_country',
                                            self.app_response)

        if self.sqlHandlerObj is None:
            self.logger.info("Going to initiate sqlHandler")
            self.sqlHandlerObj = SqlQueryHandler(self.logger)

        return self.sqlHandlerObj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sqlHandlerObj.cleanup()



'''
The above code defines a Python class Country_details, which is responsible for handling database queries related to
 the country table. It also defines a nested class SqlQueryHandler within Country_details, which is used to execute SQL queries on the database.

The code starts with importing required modules such as os, sys, sqlalchemy, flask, and others. 
It then loads the environment variables required for the database connection using the load_dotenv method from the dotenv module.

The Country_details class has an __init__ method, which takes a logger object as an argument.
 If no logger object is provided, it uses a default logger object named applog defined in the log_config module.
  The __init__ method also initializes a sqlHandlerObj object to None.

The Country_details class defines two methods, __enter__ and __exit__, which allow it to be used as a context manager. 
The __enter__ method returns an instance of the SqlQueryHandler class, which is used to execute SQL queries. 
If the sqlHandlerObj object is None, it creates a new instance of the SqlQueryHandler class and sets it to sqlHandlerObj. 
If sqlHandlerObj is not None, it returns the existing instance.

The SqlQueryHandler class has an __init__ method that takes a logger object as an argument. 
If no logger object is provided, it uses the default logger object applog defined in the log_config module. 
The __init__ method also creates a connection string using the environment variables for the database connection and initializes 
some instance variables such as session, connection, engine, and app_response. The engine object is stored in the Flask application 
context object cp.config so that it can be reused across multiple requests.

The SqlQueryHandler class defines a method get_country which connects to the database, executes an SQL query to
 retrieve details of the country table, and returns a response object with the data. It also handles exceptions and 
 sets appropriate response messages in case of any errors.

The SqlQueryHandler class defines a cleanup method which closes the session and connection objects.

Finally, the __exit__ method of the Country_details class calls the cleanup method of the SqlQueryHandler object 
to release the database resources acquired during the query execution.

'''