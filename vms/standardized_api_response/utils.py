from rest_framework import exceptions, status
from rest_framework.response import Response


def response_template(data=None, status=status.HTTP_200_OK, success=True, message=[]):
    response_dict = {
        'success': success,
        'data': data,
        'errors': message
    }
    return Response(status=status, data=response_dict)


def success_response(data=None):
    return response_template(data)


def general_error_response(message, data=None):
    """Indicating that request parameters or payload failed valication"""
    return response_template(
        data, status.HTTP_400_BAD_REQUEST, False, [message])


def created_response(data=None):
    """Indicating update using post, patch, or put was successful"""
    return response_template(data, status.HTTP_201_CREATED)
