from rest_framework import serializers
from users.models import User
from django.db import models
from users.services import user_service

class CmsListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","email", "balance", "username", "email_verified_at", "role"]


class CmsUserRoleUpdateSerializer(serializers.Serializer):
    class UserRole(models.TextChoices):
        ADMIN = "admin", "Admin"
        MEMBER = "member", "Member"
        
    user_id = serializers.IntegerField(required=True) 
    role = serializers.ChoiceField(choices=UserRole.choices, required=True)  

    def validate(self, data):
        user = user_service.get(data['user_id'])
        if user is None:
            raise serializers.ValidationError("Không tìm thấy người dùng.")
        return data