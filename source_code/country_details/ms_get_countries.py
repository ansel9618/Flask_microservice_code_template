import sys
import os
from flask import make_response, jsonify, request
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) , 'source_code'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'source_code'))
from common.app_blueprint import AppBP
bp_get_country = AppBP('bp_get_country',__name__)
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'validation_schemas'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'country_messages'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log_config'))
from utilities import Utils
from app_response import AppResponse
from source_code.common.string_table import AppMessages
from source_code.sql.country_details_sql import Country_details as sqlhandleronboarding
from source_code.country_messages.Cmessages import Messages
from marshmallow import ValidationError
from utilities  import headers_validation
from log_config.log_data import ApplicationLogger as applog
from validation_schemas.city_state_validation import ValidateCityStateSchema as validate_schema
import json

@bp_get_country.route('/',methods=['GET'])

def get_country():
    """
    gets  list of country code and name
    """
    applog.info(' get_stages ')
    app_response = AppResponse()
    applog.debug("***************************Starting to get all stages************************")
    try:
        headers = request.headers
        applog.info(f"GET ALL STAGES | Successfully received header {headers}")

        if headers.get("deviceType") and headers.get("appVersion") and headers.get("Content-Type") and \
                headers.get("deviceId") and headers.get("device") and headers.get("Authorization"):
            app_response = headers_validation(headers)
            if app_response["code"] == 200:
                data = json.loads(request.data)
                schema_validate=validate_schema().load(data)
                applog.info("GET ALL countries | get_stages method ")
                app_response = get_countries_mgr()
                if app_response['code'] == 200:
                    applog.info("GET ALL countries | get_stages response status = success")
                else:
                    applog.info("GGET ALL countries | get_stages response status = failure")
            else:
                applog.info("GET ALL countries | Authorization token is Invalid/Expired")
        else:
            applog.error("GET ALL countries | Contain insufficient headers")
            app_response.set_response(500, {}, Messages.HEADER_CONTAINS,
                                      Messages.FALSE)

    except ValidationError as ve:
        Utils.process_exception(
            ve,
            applog,
            f'Validation Error: {list(ve.messages.values())[0][0]}',
            app_response,
            False,
            400
       )

    except Exception as exp:
            Utils.process_exception(
                exp,
                applog,
                f'{AppMessages.INTERNAL_ERROR} during listing states',
                app_response
            )
    finally:
        applog.info(f"GET ALL STAGES | Ending Get States {app_response}=================")

    return make_response(jsonify(app_response), app_response['code'])


def get_countries_mgr():
    applog .info('inside get_stages_mgr')
    resp = AppResponse()
    try:
        with sqlhandleronboarding(applog) as sql_handler_obj:
            applog.info("GET ALL countries| Calling sqlHandler object, enter get_stages_mgr function")
            app_response = sql_handler_obj.get_country()
            if app_response['code'] == 200:  # checking the response code
                resp.set_response(200, app_response['data'], Messages.COUNTRY_LIST_SUCCESS, Messages.TRUE)
            else:
                applog.info("GET ALL countries| failed to return countries")
            applog.info("GET ALL countries | Ended sqlHandler object, enter get_state function")

    except Exception as excp:
        Utils.process_exception(
            excp,
            applog,
            f'{AppMessages.INTERNAL_ERROR} during fetching states list',
            resp
        )
    finally:
        applog.info("GET ALL STAGES | completed CustomerProfileMgr.get_state")
    return resp

''' 
----------------------DOC------------------------
This code defines a Flask route at the endpoint '/'. When a GET request is made to this endpoint, it calls the get_country() function.
get_country() function validates the headers of the request, if headers are valid, then it loads and validates the request 
data using the marshmallow schema ValidateCityStateSchema. If the data is valid, it calls the get_countries_mgr() function to
 retrieve a list of country codes and names from the database. If the data retrieval is successful, the get_country() function
  sets the app_response object with a success message and the data retrieved, otherwise it sets it with a failure message.

get_countries_mgr() function connects to the database using the sqlhandleronboarding class and retrieves a list of countries.
 If the data retrieval is successful, the function sets the resp object with a success message and the data retrieved, otherwise it sets it with a failure message.

This code imports various modules such as sys, os, flask, json, marshmallow, and logging, and several classes, functions, 
and constants defined in other files in the project. It also uses a logger defined in log_config/log_data.py for logging.
'''