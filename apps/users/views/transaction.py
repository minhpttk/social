from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.transaction import TransactionHistory
from users.serializers.transaction import CmsUpdateUserBalanceSerializer
from users.services import user_service
from core.permissions import IsAdminUser


class CmsUpdateUserBalanceView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = CmsUpdateUserBalanceSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            amount = serializer.validated_data['amount']
            transaction_type = serializer.validated_data['transaction_type']
            
            user = user_service.get(user_id)
            if transaction_type == 'plus':
                user.balance += amount
            elif transaction_type == 'minus':
                user.balance -= amount
            
            user.save()
            TransactionHistory.objects.create(
                user=user,
                amount=amount,
                transaction_type=transaction_type
            )

            return Response({"message": "Cập nhật số dư thành công"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

