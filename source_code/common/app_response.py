from string_table import AppMessages
from app_constants import AppConstants


class AppResponse(dict):
    def __init__(self, code_param =AppConstants.UNSUCCESSFULL_STATUS_CODE, data_param={},
                 message_param=AppMessages.FAILED, status_param=AppMessages.FALSE):
        dict.__init__(self, code=code_param, data=data_param, message=message_param, status=status_param)

    def set_response(self, code_param, data_param, message_param, status_param):
        self['code'] = code_param
        self['data'] = data_param
        self['message'] = message_param
        self['status'] = status_param
