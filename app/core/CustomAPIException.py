from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'Custom API exception occurred.'
    default_code = 'custom_api_exception'
