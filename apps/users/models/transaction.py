from django.db import models
from django.conf import settings
from core.models import TimestampsModel, SoftDeleteModel


class TransactionHistory(SoftDeleteModel, TimestampsModel):
    TRANSACTION_TYPE_CHOICES = [
        ('plus', 'Plus'),
        ('minus', 'Minus'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)

    class Meta:
        db_table = "transaction_history"

    def __str__(self):
        return f"{self.user.email} - {self.transaction_type} - {self.amount} "