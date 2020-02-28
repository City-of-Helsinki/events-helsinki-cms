from wagtail.core.models import Page


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

    class Meta:
        verbose_name = 'Collection'
