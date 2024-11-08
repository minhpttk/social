from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import auth
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = auth.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "data" : serializer.data
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = auth.LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

class GoogleLoginAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        client_id = settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id']

        try:
            # Xác thực ID token
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            # Kiểm tra issuer
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            
            print("Thông tin người dùng: ", idinfo)
            # Lấy thông tin người dùng từ token
            email = idinfo['email']
            name = idinfo.get('name', '')

            # Tìm hoặc tạo người dùng
            user, created = User.objects.get_or_create(email=email, defaults={'username': email, 'first_name': name})

            print(user) 
            print(f"User {user} created: {created}")
            # Tạo hoặc lấy token cho người dùng
            token, _ = AuthToken.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        except google_exceptions.GoogleAuthError as e:
            print(f"Google Auth Error: {e}")
            return Response({'error': f'Google Auth Error: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            print(f"Value Error: {e}")
            return Response({'error': f'Invalid token: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            import traceback
            traceback.print_exc()
            return Response({'error': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
