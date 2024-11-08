from rest_framework import status
from rest_framework.response import Response

from core.config import error_code


def login_failed_response():
    response = Response({
        "status": False,
        'message': 'Tên người dùng hoặc mật khẩu không chính xác',
    }, status.HTTP_401_UNAUTHORIZED)

    return response


def invalid_two_factor_code_response():
    return Response({
        "status": False,
        "error_code": error_code.INVALID_TWO_FACTOR_CODE,
        "message": "Invalid two-factor code"
    }, status.HTTP_400_BAD_REQUEST)


def invalid_otp_code_response():
    return Response({
        "status": False,
        "error_code": error_code.INVALID_OTP_CODE,
        "message": "Invalid OTP code"
    }, status.HTTP_400_BAD_REQUEST)


def invalid_reset_password_token_response():
    return Response({
        "status": False,
        "error_code": error_code.INVALID_RESET_PASSWORD_TOKEN,
        "message": "Invalid Reset Token"
    }, status.HTTP_400_BAD_REQUEST)


def invalid_auth_ticket_response():
    return Response({
        "status": False,
        "error_code": error_code.INVALID_AUTH_TICKET,
        "message": "Invalid authentication ticket"
    }, status.HTTP_400_BAD_REQUEST)


def insufficient_balance_response():
    return Response({
        "status": False,
        "error_code": error_code.INSUFFICIENT_BALANCE,
        "message": "Insufficient balance"
    }, status.HTTP_402_PAYMENT_REQUIRED)


def insufficient_profile_balance_response():
    return Response({
        "status": False,
        "error_code": error_code.INSUFFICIENT_PROFILE_BALANCE,
        "message": "Insufficient profile balance"
    }, status.HTTP_402_PAYMENT_REQUIRED)


def workspace_user_exist_response():
    return Response({
        "status": False,
        "error_code": error_code.WORKSPACE_USER_EXIST,
        "message": "User already exists in the workspace"
    }, status.HTTP_400_BAD_REQUEST)


def invite_request_exist_response():
    return Response({
        "status": False,
        "error_code": error_code.INVITE_REQUEST_EXIST,
        "message": "Invitation has been sent to this user."
    }, status.HTTP_400_BAD_REQUEST)


def not_have_permission_response(message="You don't have permission to access this resource."):
    return Response({
        "status": False,
        "http_code": status.HTTP_403_FORBIDDEN,
        "message": message
    }, status.HTTP_403_FORBIDDEN)


def self_invite_error_response():
    return Response({
        "status": False,
        "error_code": error_code.SELF_INVITE,
        "message": "Can not invite yourself."
    }, status.HTTP_400_BAD_REQUEST)


def delete_my_workspace_error_response():
    return Response({
        "status": False,
        "error_code": error_code.DELETE_MY_WORKSPACE,
        "message": "Cannot delete my workspace."
    }, status.HTTP_400_BAD_REQUEST)
