from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel


class HelsinkiActivities(Page):
    parent_page_types = ['wagtailcore.Page']
    subpage_typed = ['application.CollectionsGroup', 'application.LandingPage']
    max_count = 1

    class Meta:
        verbose_name = 'Helsinki Activities Service'


class CollectionsGroup(Page):
    parent_page_types = ['application.HelsinkiActivities']
    subpage_typed = ['application.Collections']
    max_count = 1

    class Meta:
        verbose_name = 'Collection Group'


class LandingPage(Page):
    parent_page_types = ['application.HelsinkiActivities']
    subpage_typed = []
    max_count = 1

    title_fi = models.CharField(max_length=255, null=True)
    title_sv = models.CharField(max_length=255, null=True)
    # title comes from Page class itself

    description_fi = models.TextField(null=True)
    description_sv = models.TextField(null=True)
    description_en = models.TextField(null=True)

    button_text_fi = models.CharField(max_length=255, null=True)
    button_text_sv = models.CharField(max_length=255, null=True)
    button_text_en = models.CharField(max_length=255, null=True)

    button_url_fi = models.URLField(max_length=500, null=True)
    button_url_sv = models.URLField(max_length=500, null=True)
    button_url_en = models.URLField(max_length=500, null=True)

    meta_information_fi = models.TextField(null=True)
    meta_information_sv = models.TextField(null=True)
    meta_information_en = models.TextField(null=True)

    page_title_fi = models.CharField(max_length=255, null=True)
    page_title_sv = models.CharField(max_length=255, null=True)
    page_title_en = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'Landing Page'

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title_fi'),
                FieldPanel('title_sv'),
                FieldPanel('title'),
            ],
            heading="Title",
            help_text='Help text number 1',
        ),
        MultiFieldPanel(
            [
                FieldPanel('description_fi'),
                FieldPanel('description_sv'),
                FieldPanel('description_en'),
            ],
            heading="Description",
            help_text='Help text number 2',
        ),
        MultiFieldPanel(
            [
                FieldPanel('button_text_fi'),
                FieldPanel('button_text_sv'),
                FieldPanel('button_text_en'),
            ],
            heading="Button Text",
            help_text='Help text number 3',
        ),
        MultiFieldPanel(
            [
                FieldPanel('button_url_fi'),
                FieldPanel('button_url_sv'),
                FieldPanel('button_url_en'),
            ],
            heading="Button Url",
            help_text='Help text number 4',
        ),
        MultiFieldPanel(
            [
                FieldPanel('meta_information_fi'),
                FieldPanel('meta_information_sv'),
                FieldPanel('meta_information_en'),
            ],
            heading="Meta Information",
            help_text='Help text number 5',
        ),
        MultiFieldPanel(
            [
                FieldPanel('page_title_fi'),
                FieldPanel('page_title_sv'),
                FieldPanel('page_title_en'),
            ],
            heading="Page Title",
            help_text='Help text number 6',
        ),
    ]


class Collections(Page):
    parent_page_types = ['application.CollectionsGroup']
    subpage_typed = []
    color_choices = [
        ('SUMU', 'Sumu'),
        ('ENGEL', 'Engel'),
        ('KUPARI', 'Kupari'),
        ('SUOMENLINNA', 'Suomenlinna'),
    ]

    box_color = models.CharField(max_length=255, choices=color_choices, null=True)

    title_fi = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otsikko FI')
    title_sv = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otsikko SV')
    # title comes from Page class itself

    description_fi = models.TextField(null=True, blank=True, verbose_name='Kuvaus FI')
    description_sv = models.TextField(null=True, blank=True, verbose_name='Kuvaus SV')
    description_en = models.TextField(null=True, blank=True, verbose_name='Kuvaus EN')

    link_text_fi = models.CharField(max_length=255, null=True, blank=True, verbose_name='Linkki teskti FI')
    link_text_sv = models.CharField(max_length=255, null=True, blank=True, verbose_name='Linkki teskti SV')
    link_text_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='Linkki teskti EN')

    link_url_fi = models.URLField(max_length=500, null=True, blank=True, verbose_name='Linkki suomenkieliselle sivulle')
    link_url_sv = models.URLField(max_length=500, null=True, blank=True, verbose_name='Linkki ruotsinkieliselle sivulle')
    link_url_en = models.URLField(max_length=500, null=True, blank=True, verbose_name='Linkki englanninkieliselle sivulle')

    social_media_description_fi = models.TextField(null=True, blank=True, verbose_name='Some-kuvaus FI')
    social_media_description_sv = models.TextField(null=True, blank=True, verbose_name='Some-kuvaus SV')
    social_media_description_en = models.TextField(null=True, blank=True, verbose_name='Some-kuvaus EN')

    curated_events_title_fi = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tapahtumien otsikko FI')
    curated_events_title_sv = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tapahtumien otsikko SV')
    curated_events_title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tapahtumien otsikko EN')

    curated_events = StreamField([
        ('event_link', blocks.URLBlock()),
    ], null=True, verbose_name='Suositeltavat tapahtumat')

    event_list_title_fi = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tapahtumien otsikko FI')
    event_list_title_sv = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tapahtumien otsikko SV')
    event_list_title_en = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tapahtumien otsikko EN')

    event_list_query = models.URLField(max_length=500, null=True, verbose_name='Hakutulossivun www-osoite')

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('box_color'),
            ],
            heading="Box Color",
            help_text='Help text number 0',
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_fi'),
                FieldPanel('title_sv'),
                FieldPanel('title'),
            ],
            heading="OTSIKKO",
            help_text='Tähän tulee kokoelmasi pääotsikko. Pidäthän otsikon lyhyenä ja ytimekkäänä.',
        ),
        MultiFieldPanel(
            [
                FieldPanel('description_fi'),
                FieldPanel('description_sv'),
                FieldPanel('description_en'),
            ],
            heading="KOKOELMAN KUVAUS",
            help_text='Pääotsikon alle tuleva teksti, joka kertoo lisää kokoelmasta ja inspiroi käyttäjiä tutustumaan suosituksiin.',
        ),
        MultiFieldPanel(
            [
                FieldPanel('link_text_fi'),
                FieldPanel('link_text_sv'),
                FieldPanel('link_text_en'),
            ],
            heading="LINKKITEKSTI",
            help_text='Vapaaehtoinen linkki, joka ohjaa lukijan pois kokoelmasta. Käytä vain harkitusti ja pidä linkkiteksti lyhyenä.',
        ),
        MultiFieldPanel(
            [
                FieldPanel('link_url_fi'),
                FieldPanel('link_url_sv'),
                FieldPanel('link_url_en'),
            ],
            heading="LINKIN WWW-OSOITE",
            help_text='Jos lisäsit aikaisempaan \'Linkkiteksti\'-osioon linkin, lisää tähän kenttään www-osoite, johon käyttäjä ohjataan.',
        ),
        MultiFieldPanel(
            [
                FieldPanel('social_media_description_fi'),
                FieldPanel('social_media_description_sv'),
                FieldPanel('social_media_description_en'),
            ],
            heading="KUVAUS SOSIAALISEEN MEDIAAN",
            help_text='Tämä teksti näkyy, kun käyttäjä jakaa kokoelman sosiaalisessa mediassa. Max. 160 merkkiä pitkä teksti, joka houkuttelee avaamaan linkin.',
        ),
        MultiFieldPanel(
            [
                FieldPanel('curated_events_title_fi'),
                FieldPanel('curated_events_title_sv'),
                FieldPanel('curated_events_title_en'),
            ],
            heading="SUOSITELTAVIEN TAPAHTUMIEN OTSIKKO",
            help_text='Kirjoita tähän otsikko, jonka haluat näyttää käsin poimittavien, suositeltavien tapahtumien yläpuolella.',
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel('curated_events'),
            ],
            heading="SUOSITELTAVAT TAPAHTUMAT",
            help_text='Lisää tähän ne tapahtumat, joita haluat suositella käyttäjälle. Tapahtumat näkyvät siinä järjestyksessä, jossa syötät ne. Voit helposti lisätä uusia tapahtumia, poistaa niitä ja muuttaa järjestystä. Mene haluamasi tapahtuman sivulle, kopioi sen www-osoite ja liitä osoite alla olevaan kenttään.',
        ),
        MultiFieldPanel(
            [
                FieldPanel('event_list_title_fi'),
                FieldPanel('event_list_title_sv'),
                FieldPanel('event_list_title_en'),
            ],
            heading="MUIDEN TAPAHTUMIEN OTSIKKO",
            help_text='Käsin poimittujen tapahtumien voit tässä suositella muita samankaltaisia tai muuten kiinnostavia tapahtumia. Näille tapahtumille tarvitaan oma otsikko, esim. "Tutustu myös näihin".',
        ),
        MultiFieldPanel(
            [
                FieldPanel('event_list_query'),
            ],
            heading="TAPAHTUMALISTAUKSEN HAUN WWW-OSOITE",
            help_text='Tee tapahtumahaku sopivilla hakukriteereillä tapahtumat.helsingissa. Kun hakutuloksessa on haluamasi tapahtumat, kopioi hakutuloksen www-osoite tähän kenttään.',
        ),
    ]

    class Meta:
        verbose_name = 'Collection'
