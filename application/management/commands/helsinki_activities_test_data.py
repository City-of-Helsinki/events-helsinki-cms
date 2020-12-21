import os
import shutil

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

    "event_list_query_fi": "http://localhost:3000/fi/events?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",
    "event_list_query_sv": "http://localhost:3000/sv/events?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",
    "event_list_query_en": "http://localhost:3000/en/events?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",

    "course_list_query_fi": "http://localhost:3000/fi/courses?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",
    "course_list_query_sv": "http://localhost:3000/sv/courses?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",
    "course_list_query_en": "http://localhost:3000/en/courses?categories=music&districts=kaupunginosa%3Aetu-%B6l%C3%B6",

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
    "title_en": "Very cool English title",
}

LANDING_PAGE_BASE = {
    "title_fi": "Syksyn riehakkaimmat riennot",
    "title_sv": "Höstens mest livliga knep",
    "title_en": "Very cool English title",

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


ABOUT_PAGE_BASE = {
    "heading_section_fi": "Heading Section in FI",
    "heading_section_sv": "Heading Section in SV",
    "heading_section_en": "Heading Section in EN",

    "content_section_fi": "Content Section in FI",
    "content_section_sv": "Content Section in SV",
    "content_section_en": "Content Section in EN",
}


ACCESSIBILITY_PAGE_BASE = {
    "heading_section_fi": "Heading Section in FI",
    "heading_section_sv": "Heading Section in SV",
    "heading_section_en": "Heading Section in EN",

    "content_section_fi": "Content Section in FI",
    "content_section_sv": "Content Section in SV",
    "content_section_en": "Content Section in EN",
}


class Command(BaseCommand):
    help = "A management command used to populate Helsinki Activities test data into the CMS"

    def handle(self, *args, **options):
        if settings.DEBUG is not True:
            raise CommandError('This command can be run only in DEBUG mode')

        # Delete all pages and images
        wagtail_models.Page.objects.get(title='Root').get_children().delete()
        models.CustomImage.objects.all().delete()
        wagtail_models.Site.objects.all().delete()

        os.makedirs('media-files', exist_ok=True)

        # Saving images to database
        shutil.copy2('pictures/gerome-bruneau-RPmWEtZLh7U-unsplash.jpg', 'media-files/collection_hero_image.jpg')
        collection_hero_image = models.CustomImage(title='Collection Hero Image', file='collection_hero_image.jpg', photographer_credit='gerome-bruneau')
        collection_hero_image.save()

        shutil.copy2('pictures/davisco-5E5N49RWtbA-unsplash.jpg', 'media-files/landing_page_hero_background_image.jpg')
        hero_background_image = models.CustomImage(title='Landing Page Hero Background Image', file='landing_page_hero_background_image.jpg', photographer_credit='davisco')
        hero_background_image.save()

        shutil.copy2('pictures/ravi-sharma-xxGyLaY4v14-unsplash.jpg', 'media-files/landing_page_hero_background_image_mobile.jpg')
        hero_background_image_mobile = models.CustomImage(title='Landing Page Hero Background Image Mobile', file='landing_page_hero_background_image_mobile.jpg', photographer_credit='ravi-sharma')
        hero_background_image_mobile.save()

        shutil.copy2('pictures/joanna-kosinska-1_CMoFsPfso-unsplash.jpg', 'media-files/landing_page_hero_top_layer_image.jpg')
        hero_top_layer_image = models.CustomImage(title='Landing Page Hero Top Layer Image', file='landing_page_hero_top_layer_image.jpg', photographer_credit='joanna-kosinska')
        hero_top_layer_image.save()

        shutil.copy2('pictures/merakist-CNbRsQj8mHQ-unsplash.jpg', 'media-files/landing_page_social_media_image.jpg')
        social_media_image = models.CustomImage(title='Landing Page Social Media Image', file='landing_page_social_media_image.jpg', photographer_credit='merakist')
        social_media_image.save()

        root_page = wagtail_models.Page.objects.get(title='Root')

        helsinki_activities = root_page.add_child(instance=models.HelsinkiActivities(title='Helsinki Activities'))

        collections_folder = helsinki_activities.add_child(instance=models.CollectionsFolder(title='Collections'))
        landing_pages_folder = helsinki_activities.add_child(instance=models.LandingPagesFolder(title='Landing Pages'))
        static_pages_folder = helsinki_activities.add_child(instance=models.StaticPagesFolder(title='Static Pages'))

        collections_folder.add_child(instance=models.Collections(
            title='Kool Kids of Kallio', **dict(COLLECTION_BASE, hero_image=collection_hero_image)))

        collections_folder.add_child(instance=models.Collections(
            title='Kool Kids of Kamppi', **dict(COLLECTION_BASE, visible_on_frontpage=False)))

        collections_folder.add_child(instance=models.Collections(
            title='Kool Kids of Kurvi', **COLLECTION_BASE))

        landing_pages_folder.add_child(instance=models.LandingPages(
            title='Summer is here!', **dict(LANDING_PAGE_BASE, hero_background_image_fi=hero_background_image, hero_background_image_mobile_fi=hero_background_image_mobile, hero_top_layer_image_fi=hero_top_layer_image, social_media_image_fi=social_media_image)))

        landing_pages_folder.add_child(instance=models.LandingPages(
            title='Fall is here!', **LANDING_PAGE_BASE))

        landing_pages_folder.add_child(instance=models.LandingPages(
            title='Winter is here!', **LANDING_PAGE_BASE))

        static_pages_folder.add_child(instance=models.AboutPage(title='About', **ABOUT_PAGE_BASE))
        static_pages_folder.add_child(instance=models.AccessibilityPage(title='Accessibility', **ACCESSIBILITY_PAGE_BASE))

        # Creating a default "Site"
        default_site = wagtail_models.Site(hostname='localhost', port='8080', root_page=helsinki_activities, is_default_site=True)
        default_site.save()

        self.stdout.write('Helsinki Activities test data were populated to CMS')
