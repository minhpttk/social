from django.core.management import BaseCommand

from transaction.models import Transaction


class Command(BaseCommand):
    help = "Update recharge status"

    def handle(self, *args, **kwargs):
        transactions = Transaction.objects.filter(
            status=Transaction.Status.PENDING,
            transaction_type=Transaction.TransactionType.RECHARGE
        )
