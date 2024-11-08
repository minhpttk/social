from rest_framework import serializers
from users.models import User
from users.validator.auth import  validate_password, validate_login_data

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email','password','confirm_password', 'username')
        extra_kwargs = {
            'password': {'write_only': True}
            
        }

    def validate(self, data):
        
        return validate_password(data)

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User(**validated_data)
        user.set_password(validated_data['password']) 
        user.save()
        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        return validate_login_data(data)




    
