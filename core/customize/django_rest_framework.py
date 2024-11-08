from rest_framework.views import exception_handler
from rest_framework import exceptions


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, exceptions.APIException) and isinstance(exc.detail, (list, dict)):
        response.data = {
            "error_fields": response.data
        }

    return response
