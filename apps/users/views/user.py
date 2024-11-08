from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.paginator import Paginator
from math import ceil

from users.serializers.user import CmsListUserSerializer, CmsUserRoleUpdateSerializer
from users.services import user_service
from core.permissions import IsAdminUser
from core.config.paging import PAGE_NUMBER_DEFAULT, PAGE_SIZE_DEFAULT

class CmsListUserView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        filter_params = request.GET.copy()
        list_user = user_service.get_list()
        total_record = list_user.count()
        page_number = filter_params.get("page_num", PAGE_NUMBER_DEFAULT)
        page_size = filter_params.get("page_size", PAGE_SIZE_DEFAULT)
        page_total = ceil(len(list_user) / int(page_size))
        paginator = Paginator(list_user, page_size)

        serializer = CmsListUserSerializer(paginator.page(page_number), many=True)

        return Response(
            {
                "data": serializer.data,
                "page_number": int(page_number),
                "page_size": int(page_size),
                "page_total": page_total,
                "total_record": total_record
            }
        )
    

class CmsUserRoleUpdateView(APIView):
    permission_classes = (IsAdminUser,)

    def put(self, request):
        serializer = CmsUserRoleUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']  
            user = user_service.get(user_id)
            user.role = serializer.validated_data['role']  # Cập nhật role
            user.save()
            return Response({"user_id": user.id, "role": user.role}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
