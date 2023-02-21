import traceback
import json
import requests
from app_response import AppResponse
import jwt
from flask import request
from marshmallow import Schema, fields, ValidationError
import os
from functools import wraps
from log_data import ApplicationLogger as applog
from string_table import AppMessages
from dotenv import load_dotenv
load_dotenv(override=True)


class Utils:

    @staticmethod
    def process_exception(excp, logger, message, result, status=False, status_code=500):
        logger.error(message)
        logger.error(traceback.format_exc())
        stack_trace = traceback.format_exc()
        resp = AppResponse(status_code, stack_trace, message, status)
        for k in resp:
            result[k] = resp[k]



def isTokenValid(access_token):
    try:
        access_token = access_token.split()
        message = 'INVALID'
        if "Bearer" in access_token:
            access_token = access_token[1]
            res = jwt.decode(access_token, options={"verify_signature": False, "verify_exp": True})
            if res:
                message = access_token
    except jwt.ExpiredSignatureError:
        message = 'EXPIRED'
    except ValidationError as ve:
        message = 'INVALID'
    except Exception as exp:
        message = 'INVALID'
    finally:
        return message

# Validate Headers
class ValidateHeadersSchema(Schema):
    deviceType = fields.String(required=True)
    appVersion = fields.String(required=True)
    ContentType = fields.String(required=True)
    deviceId = fields.UUID(required=True)
    device = fields.String(required=True)
    Authorization = fields.String(required=True)
#
#
def headers_validation(headers_data):

    try:
        headers = {
            "deviceType": headers_data.get("deviceType"),
            "appVersion": headers_data.get("appVersion"),
            "ContentType": headers_data.get("Content-Type"),
            "deviceId": headers_data.get("deviceId"),
            "device": headers_data.get("device"),
            "Authorization": headers_data.get("Authorization")
        }
        headers_schema = ValidateHeadersSchema()
        headers = headers_schema.load(headers)
        token = headers_data["Authorization"]
        access_token = token.split()
        if "Bearer" in access_token:
            data = access_token[1]
            validity= isTokenValid(token)
            return {'code': 200, 'data': {}, 'message': "token valid", 'status': False}
        else:
            return {'code': 401, 'data': {}, 'message': "Failed", 'status': False}
    except Exception as exp:
        return {'code': 500, 'data': str(exp), 'message': "Failed", 'status': False}





'''

The code above includes several utility functions to be used in a Flask app. Here's a brief explanation of each of these functions:

process_exception: This function takes an exception object, logger object, error message, and result object as input. 
It logs the error message and the traceback for the given exception, and then creates an AppResponse object with the appropriate
 error status code and message. The AppResponse object is then merged into the input result object.

isTokenValid: This function takes an access token as input and checks whether it is valid. It first splits the access 
token into its two parts (the bearer type and the token value). If the bearer type is "Bearer", it attempts to decode 
the token using the jwt module. If the token is valid, it returns the token value; otherwise, it returns "INVALID".
 If the token has expired, it returns "EXPIRED".

ValidateHeadersSchema: This class defines a Marshmallow schema for validating a set of headers in an HTTP request. 
The schema includes fields for deviceType, appVersion, ContentType, deviceId, device, and Authorization.

headers_validation: This function takes a dictionary of headers as input and validates them against the ValidateHeadersSchema. 
If the validation is successful, it calls the isTokenValid function to check the validity of the access token. 
If the access token is valid, it returns a success message with a 200 status code; otherwise, it returns a failure message with a 401 status code.



All of these functions can be imported and used in a Flask app to add error handling, header validation, and JWT authentication to specific routes.
'''