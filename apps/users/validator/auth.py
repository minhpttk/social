from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User
def validate_password(data):
    password = data["password"]
    if len(password) < 6:
        raise serializers.ValidationError("Mật khẩu tối thiểu 6 ký tự")
    return data


def validate_login_data(data):
    username = data.get('username')
    password = data.get('password')

    if username and password:
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                raise serializers.ValidationError("Sai tài khoản hoặc mật khẩu")
        else:
            user = None
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError("Sai tài khoản hoặc mật khẩu")

        if user and not user.check_password(password):
            raise serializers.ValidationError("Sai tài khoản hoặc mật khẩu")

    else:
        raise serializers.ValidationError("Yêu cầu điền đầy đủ thông tin đăng nhập")

    data['user'] = user
    return data 