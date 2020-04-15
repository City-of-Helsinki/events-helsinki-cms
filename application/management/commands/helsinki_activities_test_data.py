from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from wagtail.core import models as wagtail_models

from application import models

COLLECTION_BASE = {
    "visible_on_frontpage": True,

    "box_color": "SUOMENLINNA",

    "curated_events": [
        ('event_link', "http://localhost:3000/fi/event/helsinki:afxh3naida?id=123"),
        ('event_link', "http://localhost:3000/fi/event/helsinki:afxrsql3xa"),
        ('event_link', "http://localhost:3000/fi/event/helsinki:afxh3namhe"),
        ('event_link', "http://localhost:3000/fi/event/helsinki:afxpj6bxbu"),
        ('event_link', "http://localhost:3000/fi/event/helsinki:afx5msunhu"),
    ],

    "curated_events_title_en": "At least visit these",
    "curated_events_title_fi": "Käy ainakin näissä",
    "curated_events_title_sv": "Besök åtminstone dessa",

    "description_en": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero",
    "description_fi": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero",
    "description_sv": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero",

    "social_media_description_en": "social media is social. eget condimentum rhoncus, sem quam semper libero",
    "social_media_description_fi": "social media is social. eget condimentum rhoncus, sem quam semper libero",
    "social_media_description_sv": "social media is social. eget condimentum rhoncus, sem quam semper libero",

    "event_list_query": "http://localhost:3000/en/events?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",

    "event_list_title_en": "All the best events of the fall",
    "event_list_title_fi": "Kaikki syksyn parhaat tapahtumat",
    "event_list_title_sv": "Höstens bästa händelser",

    "link_text_en": "Read more on the project website",
    "link_text_fi": "Lue lisää hankkeen omilta sivuilta",
    "link_text_sv": "Läs mer på projektets webbplats",

    "link_url_en": "http://www.google.com",
    "link_url_fi": "http://www.google.com",
    "link_url_sv": "http://www.google.com",

    "title_fi": "Syksyn riehakkaimmat riennot",
    "title_sv": "Höstens mest livliga knep",
}

LANDING_PAGE_BASE = {
    "visible_on_frontpage": False,

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
    help = "A management command used to populate Helsinki Activities test data into the CMS"

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError('This command can be run only in DEBUG mode')

        wagtail_models.Page.objects.get(title='Root').get_children().delete()

        root_page = wagtail_models.Page.objects.get(title='Root')

        helsinki_activities = root_page.add_child(instance=models.HelsinkiActivities(title='Helsinki Activities'))

        collections_folder = helsinki_activities.add_child(instance=models.CollectionsFolder(title='Collections'))
        landing_pages_folder = helsinki_activities.add_child(instance=models.LandingPagesFolder(title='Landing Pages'))

        collections_folder.add_child(instance=models.Collections(
            title='Kool Kids of Kallio', **COLLECTION_BASE))
        collections_folder.add_child(instance=models.Collections(
            title='Kool Kids of Kamppi', **dict(COLLECTION_BASE, visible_on_frontpage=False)))
        collections_folder.add_child(instance=models.Collections(
            title='Kool Kids of Kurvi', **COLLECTION_BASE))

        landing_pages_folder.add_child(instance=models.LandingPages(
            title='Summer is here!', **dict(LANDING_PAGE_BASE, visible_on_frontpage=True)))
        landing_pages_folder.add_child(instance=models.LandingPages(
            title='Fall is here!', **LANDING_PAGE_BASE))
        landing_pages_folder.add_child(instance=models.LandingPages(
            title='Winter is here!', **LANDING_PAGE_BASE))

        self.stdout.write('Helsinki Activities test data were populated to CMS')
