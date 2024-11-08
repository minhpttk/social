from rest_framework import serializers
from users.services import user_service

def validate_amount(data):
    amount = data['amount']
    if amount <= 0:
        raise serializers.ValidationError("Số tiền phải lớn hơn 0.")  

def validate_user(data):
    user = user_service.get(data['user_id'])
    if user is None:
        raise serializers.ValidationError("Không tìm thấy người dùng.")
    
def validate_balance(data):
    user = user_service.get(data['user_id'])
    if data['transaction_type'] == 'minus':
        if user.balance - data['amount'] <= 0:
            raise serializers.ValidationError("Số dư tài khoản nhỏ hơn 0. Không thể thực hiện.")