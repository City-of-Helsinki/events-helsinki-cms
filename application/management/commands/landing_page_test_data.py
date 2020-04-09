from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from wagtail.core import models as wagtail_models

from application import models

LANDING_PAGE_BASE = {
    "title_fi": "Syksyn riehakkaimmat riennot",
    "title_sv": "Höstens mest livliga knep",

    "description_en": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero",
    "description_fi": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero",
    "description_sv": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero",

    "button_text_en": "Read more on the project website",
    "button_text_fi": "Lue lisää hankkeen omilta sivuilta",
    "button_text_sv": "Läs mer på projektets webbplats",

    "button_url_en": "http://www.google.com",
    "button_url_fi": "http://www.google.com",
    "button_url_sv": "http://www.google.com",

    "meta_information_en": "We put together the best foliage for the fall",
    "meta_information_fi": "Kokosimme parhaat tärpit syksylle",
    "meta_information_sv": "Vi sätter ihop det bästa bladverket för hösten",

    "page_title_en": "We put together the best foliage for the fall",
    "page_title_fi": "Kokosimme parhaat tärpit syksylle",
    "page_title_sv": "Vi sätter ihop det bästa bladverket för hösten",
}


class Command(BaseCommand):
    help = "A management command used to populate the landing page into the CMS"

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError('This command can be run only in DEBUG mode')

        helsinki_activities_page = wagtail_models.Page.objects.get(title='Helsinki Activities')

        landing_pages_page = helsinki_activities_page.add_child(
            instance=models.LandingPagesFolder(title='Landing Pages'))

        landing_pages_page.add_child(instance=models.LandingPages(title='Summer is here!', **LANDING_PAGE_BASE))
        landing_pages_page.add_child(instance=models.LandingPages(title='Fall is here!', **LANDING_PAGE_BASE))
        landing_pages_page.add_child(instance=models.LandingPages(title='Winter is here!', **LANDING_PAGE_BASE))

        self.stdout.write('Populating data to CMS succeeded')
