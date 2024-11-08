from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Create a new Django app inside the apps directory'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the app to create')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']

        # Path to the directory where new apps will be created
        apps_dir_path = 'apps'

        # Create the new app inside the apps directory
        os.system(f'cd {apps_dir_path} && python ../manage.py startapp {app_name}')
