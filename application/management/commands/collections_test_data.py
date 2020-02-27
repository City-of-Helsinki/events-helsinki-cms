from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from wagtail.core import models as wagtail_models

from application import models


class Command(BaseCommand):
    help = "A management command used to populate basic collections data into the CMS"

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError('This command can be run only in DEBUG mode')

        wagtail_models.Page.objects.get(title='Root').get_children().delete()

        root_page = wagtail_models.Page.objects.get(title='Root')

        helsinki_activities_page = root_page.add_child(instance=models.HelsinkiActivities(title='Helsinki Activities'))

        collections_page = helsinki_activities_page.add_child(instance=models.CollectionsGroup(title='Collections'))

        collections_page.add_child(instance=models.Collections(title='Kool Kids of Kallio'))
        collections_page.add_child(instance=models.Collections(title='Kool Kids of Kamppi'))
        collections_page.add_child(instance=models.Collections(title='Kool Kids of Kurvi'))

        self.stdout.write('Populating data to CMS succeeded')
