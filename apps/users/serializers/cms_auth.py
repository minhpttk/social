from rest_framework import serializers

class CmsLoginSerializer(serializers.Serializer):  # noqa
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)