from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers.cms_auth import CmsLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from core.shortcuts.response import login_failed_response
from users.services import user_service

class CmsLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CmsLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        credentials = serializer.validated_data
        user = user_service.get_by_email(credentials['email'])
        if (not user) or (not user.check_password(credentials['password'])):
            return login_failed_response()
        
        refresh = RefreshToken.for_user(user)
        return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
