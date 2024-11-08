from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = "Create sample data"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str)

    def handle(self, *args, **kwargs):
        if kwargs["model_name"] == "admin_user":
            self.create_admin_user()
        if kwargs["model_name"] == "all":
            self.create_admin_user()

    def create_admin_user(self):
        User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='Abc!@#123456',
            role='admin'
        )
