from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel


class HelsinkiActivities(Page):
    parent_page_types = ['wagtailcore.Page']
    subpage_typed = ['application.CollectionsGroup']
    max_count = 1

    class Meta:
        verbose_name = 'Helsinki Activities Service'


class CollectionsGroup(Page):
    parent_page_types = ['application.HelsinkiActivities']
    subpage_typed = ['application.Collections']
    max_count = 1

    class Meta:
        verbose_name = 'Collection Group'


class Collections(Page):
    parent_page_types = ['application.CollectionsGroup']
    subpage_typed = []

    # title comes from Page class itself
    title_fi = models.CharField(max_length=255, null=True)
    title_sv = models.CharField(max_length=255, null=True)

    curated_events_title_en = models.CharField(max_length=255, null=True)
    curated_events_title_fi = models.CharField(max_length=255, null=True)
    curated_events_title_sv = models.CharField(max_length=255, null=True)

    subtitles_en = models.CharField(max_length=255, null=True)
    subtitles_fi = models.CharField(max_length=255, null=True)
    subtitles_sv = models.CharField(max_length=255, null=True)

    description_en = models.TextField(null=True)
    description_fi = models.TextField(null=True)
    description_sv = models.TextField(null=True)

    social_media_description_en = models.TextField(null=True)
    social_media_description_fi = models.TextField(null=True)
    social_media_description_sv = models.TextField(null=True)

    link_text_en = models.CharField(max_length=255, null=True, blank=True)
    link_text_fi = models.CharField(max_length=255, null=True, blank=True)
    link_text_sv = models.CharField(max_length=255, null=True, blank=True)

    link_url_en = models.URLField(max_length=200, null=True, blank=True)
    link_url_fi = models.URLField(max_length=200, null=True, blank=True)
    link_url_sv = models.URLField(max_length=200, null=True, blank=True)

    event_list_title_en = models.CharField(max_length=255, null=True)
    event_list_title_fi = models.CharField(max_length=255, null=True)
    event_list_title_sv = models.CharField(max_length=255, null=True)

    event_list_query = models.URLField(max_length=200, null=True)

    curated_events = StreamField([
        ('event_link', blocks.URLBlock()),
    ], null=True)

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('title_fi'),
                FieldPanel('title_sv'),
            ],
            heading="Title",
        ),
        MultiFieldPanel(
            [
                FieldPanel('curated_events_title_en'),
                FieldPanel('curated_events_title_fi'),
                FieldPanel('curated_events_title_sv'),
            ],
            heading="Curated Events Title",
        ),
        MultiFieldPanel(
            [
                FieldPanel('subtitles_en'),
                FieldPanel('subtitles_fi'),
                FieldPanel('subtitles_sv'),
            ],
            heading="Subtitles",
        ),
        MultiFieldPanel(
            [
                FieldPanel('description_en'),
                FieldPanel('description_fi'),
                FieldPanel('description_sv'),
            ],
            heading="Description",
        ),
        MultiFieldPanel(
            [
                FieldPanel('social_media_description_en'),
                FieldPanel('social_media_description_fi'),
                FieldPanel('social_media_description_sv'),
            ],
            heading="Social Media Description",
        ),
        MultiFieldPanel(
            [
                FieldPanel('link_text_en'),
                FieldPanel('link_text_fi'),
                FieldPanel('link_text_sv'),
            ],
            heading="Link Text",
        ),
        MultiFieldPanel(
            [
                FieldPanel('link_url_en'),
                FieldPanel('link_url_fi'),
                FieldPanel('link_url_sv'),
            ],
            heading="Link URL",
        ),
        MultiFieldPanel(
            [
                FieldPanel('event_list_title_en'),
                FieldPanel('event_list_title_fi'),
                FieldPanel('event_list_title_sv'),
            ],
            heading="Event List Title",
        ),
        FieldPanel('event_list_query'),
        StreamFieldPanel('curated_events'),
    ]

    class Meta:
        verbose_name = 'Collection'
