from rest_framework import serializers
from users.validator.transaction import validate_amount, validate_balance, validate_user
from django.db import models

class CmsUpdateUserBalanceSerializer(serializers.Serializer):
    class TransactionType(models.TextChoices):  # Tạo lớp sự chọn cho loại giao dịch
        PLUS = 'plus', 'Plus'
        MINUS = 'minus', 'Minus'

    user_id = serializers.IntegerField()
    amount = serializers.IntegerField()
    transaction_type = serializers.ChoiceField(choices=TransactionType.choices)

    def validate(self, data):
        # Thực hiện các logic kiểm tra hợp lệ của dữ liệu
        validate_user(data)
        validate_amount(data)
        validate_balance(data)

        return data
