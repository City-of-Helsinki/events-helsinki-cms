import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        SUPERUSER_PASSWORD = os.getenv('SUPERUSER_PASSWORD')

        if not SUPERUSER_PASSWORD:
            raise CommandError('SUPERUSER_PASSWORD env variable is not set')

        admin_user_exists = User.objects.filter(username='admin').exists()
        if admin_user_exists:
            self.stdout.write('Superuser "admin" already exists')
            return

        User.objects.create_superuser('admin', 'admin@admin.com', SUPERUSER_PASSWORD)
        self.stdout.write('Superuser "admin" successfully created')
