from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            pass

        admin_user_exists = User.objects.filter(username='admin').exists()
        if admin_user_exists:
            self.stdout.write('Superuser "admin" already exists')
            return

        User.objects.create_superuser('admin', 'admin@admin.com', 'coconut')
        self.stdout.write('Superuser "admin" with "coconut" password created')
