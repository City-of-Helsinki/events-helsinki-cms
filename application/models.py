from uuid import uuid4

from django.conf import settings
from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.models import AbstractImage, AbstractRendition
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    StreamFieldPanel,
    TabbedInterface,
    PageChooserPanel,
)

from application.wagtail_edit_handlers import (
    CustomImageChooserPanel as ImageChooserPanel,
)
from application.wagtail_edit_handlers import CUSTOM_SETTINGS_PANELS


class CustomImage(AbstractImage):
    photographer_credit_fi = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Kuvaajan tiedot"
    )
    photographer_credit_sv = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Fotografkredit"
    )
    photographer_credit_en = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Photographer credit"
    )

    admin_form_fields = (
        "file",
        "photographer_credit_fi",
        "photographer_credit_sv",
        "photographer_credit_en",
        "title",
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class HelsinkiActivities(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_typed = [
        "application.CollectionsFolder",
        "application.LandingPagesFolder",
        "application.StaticPagesFolder",
    ]
    preview_modes = []
    max_count = 1

    class Meta:
        verbose_name = "Helsinki Activities Service"


class CollectionsFolder(Page):
    parent_page_types = ["application.HelsinkiActivities"]
    subpage_typed = ["application.Collections"]
    preview_modes = []
    max_count = 1

    class Meta:
        verbose_name = "Collections Folder"


class LandingPagesFolder(Page):
    parent_page_types = ["application.HelsinkiActivities"]
    subpage_typed = ["application.LandingPages"]
    preview_modes = []
    max_count = 1

    class Meta:
        verbose_name = "Landing Pages Folder"


class BannerPagesFolder(Page):
    parent_page_types = ["application.HelsinkiActivities"]
    subpage_typed = ["application.BannerPages"]
    preview_modes = []
    max_count = 1

    class Meta:
        verbose_name = "Banner Pages Folder"


class StaticPagesFolder(Page):
    parent_page_types = ["application.HelsinkiActivities"]
    subpage_typed = ["application.AboutPage", "application.AccessibilityPage"]
    preview_modes = []
    max_count = 1

    class Meta:
        verbose_name = "Static Pages Folder"


class AboutPage(Page):
    parent_page_types = ["application.StaticPagesFolder"]
    subpage_typed = []
    preview_modes = []
    max_count = 1

    limited_rich_text_field_features = [
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "bold",
        "italic",
        "ol",
        "ul",
        "hr",
        "link",
    ]

    heading_section_fi = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Ingressi FI"
    )
    heading_section_sv = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Ingressi SV"
    )
    heading_section_en = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Ingressi EN"
    )

    content_section_fi = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Sisältöäalue FI"
    )
    content_section_sv = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Sisältöäalue SV"
    )
    content_section_en = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Sisältöäalue EN"
    )

    keywords_fi = StreamField(
        [
            ("keywords_fi", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords FI",
    )

    keywords_sv = StreamField(
        [
            ("keywords_sv", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords SV",
    )

    keywords_en = StreamField(
        [
            ("keywords_en", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords EN",
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel("heading_section_fi"),
                FieldPanel("heading_section_sv"),
                FieldPanel("heading_section_en"),
            ],
            heading="Ingressi",
            help_text="Tämä teksti tulee sivun ylälaitaan ja siihen on tarkoitus kirjoittaa lyhyesti sisällön ydin.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("content_section_fi"),
                FieldPanel("content_section_sv"),
                FieldPanel("content_section_en"),
            ],
            heading="Sisältöäalue",
            help_text="Tämä sisältö tulee ingressin jälkeen.",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("keywords_fi"),
                StreamFieldPanel("keywords_sv"),
                StreamFieldPanel("keywords_en"),
            ],
            heading="Keywords",
            help_text="",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Sisältö"),
            ObjectList(
                CUSTOM_SETTINGS_PANELS, heading="Asetukset", classname="settings"
            ),
        ]
    )

    def clean(self):
        self.title = "Tietoja palvelusta"
        self.slug = str(uuid4())
        super().clean()

    def get_context(self, request):
        context = super().get_context(request)
        context["FRONTEND_BASE_URL"] = settings.FRONTEND_BASE_URL
        return context

    class Meta:
        verbose_name = "About Page"


class AccessibilityPage(Page):
    parent_page_types = ["application.StaticPagesFolder"]
    subpage_typed = []
    preview_modes = []
    max_count = 1

    limited_rich_text_field_features = [
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "bold",
        "italic",
        "ol",
        "ul",
        "hr",
        "link",
    ]

    heading_section_fi = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Ingressi FI"
    )
    heading_section_sv = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Ingressi SV"
    )
    heading_section_en = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Ingressi EN"
    )

    content_section_fi = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Sisältöäalue FI"
    )
    content_section_sv = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Sisältöäalue SV"
    )
    content_section_en = RichTextField(
        features=limited_rich_text_field_features, verbose_name="Sisältöäalue EN"
    )

    keywords_fi = StreamField(
        [
            ("keywords_fi", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords FI",
    )

    keywords_sv = StreamField(
        [
            ("keywords_sv", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords SV",
    )

    keywords_en = StreamField(
        [
            ("keywords_en", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords EN",
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel("heading_section_fi"),
                FieldPanel("heading_section_sv"),
                FieldPanel("heading_section_en"),
            ],
            heading="Ingressi",
            help_text="Tämä teksti tulee sivun ylälaitaan ja siihen on tarkoitus kirjoittaa lyhyesti sisällön ydin.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("content_section_fi"),
                FieldPanel("content_section_sv"),
                FieldPanel("content_section_en"),
            ],
            heading="Sisältöäalue",
            help_text="Tämä sisältö tulee ingressin jälkeen.",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("keywords_fi"),
                StreamFieldPanel("keywords_sv"),
                StreamFieldPanel("keywords_en"),
            ],
            heading="Keywords",
            help_text="",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Sisältö"),
            ObjectList(
                CUSTOM_SETTINGS_PANELS, heading="Asetukset", classname="settings"
            ),
        ]
    )

    def clean(self):
        self.title = "Saavutettavuus"
        self.slug = str(uuid4())
        super().clean()

    def get_context(self, request):
        context = super().get_context(request)
        context["FRONTEND_BASE_URL"] = settings.FRONTEND_BASE_URL
        return context

    class Meta:
        verbose_name = "Accessibility Page"


class BannerPages(Page):
    parent_page_types = ["application.BannerPagesFolder"]
    subpage_typed = []
    preview_modes = []
    hero_background_image_color_choices = [
        ("ENGEL", "Engel"),
        ("COPPER", "Kupari"),
        ("SUOMENLINNA", "Suomenlinna"),
    ]

    title_and_description_color_choices = [
        ("BLACK", "Black"),
        ("WHITE", "White"),
    ]

    hero_background_image_fi = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuva FI",
    )
    hero_background_image_sv = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuva SV",
    )
    hero_background_image_en = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuva EN",
    )

    hero_background_image_color_fi = models.CharField(
        max_length=255,
        choices=hero_background_image_color_choices,
        null=True,
        blank=True,
        verbose_name="Pääkuvan taustaväri FI",
    )
    hero_background_image_color_sv = models.CharField(
        max_length=255,
        choices=hero_background_image_color_choices,
        null=True,
        blank=True,
        verbose_name="Pääkuvan taustaväri SV",
    )
    hero_background_image_color_en = models.CharField(
        max_length=255,
        choices=hero_background_image_color_choices,
        null=True,
        blank=True,
        verbose_name="Pääkuvan taustaväri EN",
    )

    hero_background_image_mobile_fi = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuva mobiililla FI",
    )
    hero_background_image_mobile_sv = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuva mobiililla SV",
    )
    hero_background_image_mobile_en = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuva mobiililla EN",
    )

    hero_top_layer_image_fi = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuvan päälle asettuva kuva FI",
    )
    hero_top_layer_image_sv = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuvan päälle asettuva kuva SV",
    )
    hero_top_layer_image_en = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Pääkuvan päälle asettuva kuva EN",
    )

    button_text_fi = models.CharField(
        max_length=255, null=True, verbose_name="Napin teksti FI"
    )
    button_text_sv = models.CharField(
        max_length=255, null=True, verbose_name="Napin teksti SV"
    )
    button_text_en = models.CharField(
        max_length=255, null=True, verbose_name="Napin teksti EN"
    )

    button_url_fi = models.URLField(
        max_length=500, null=True, verbose_name="Linkki suomenkieliselle sivulle"
    )
    button_url_sv = models.URLField(
        max_length=500, null=True, verbose_name="Linkki ruotsinkieliselle sivulle"
    )
    button_url_en = models.URLField(
        max_length=500, null=True, verbose_name="Linkki englanninkieliselle sivulle"
    )

    social_media_image_fi = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Some-postauksen kuva FI",
    )
    social_media_image_sv = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Some-postauksen kuva SV",
    )
    social_media_image_en = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Some-postauksen kuva EN",
    )

    title_fi = models.CharField(max_length=255, null=True, verbose_name="Otsikko FI")
    title_sv = models.CharField(max_length=255, null=True, verbose_name="Otsikko SV")
    title_en = models.CharField(max_length=255, null=True, verbose_name="Otsikko EN")

    title_and_description_color_fi = models.CharField(
        max_length=255,
        choices=title_and_description_color_choices,
        null=True,
        blank=True,
        verbose_name="Tekstin väri FI",
    )
    title_and_description_color_sv = models.CharField(
        max_length=255,
        choices=title_and_description_color_choices,
        null=True,
        blank=True,
        verbose_name="Tekstin väri SV",
    )
    title_and_description_color_en = models.CharField(
        max_length=255,
        choices=title_and_description_color_choices,
        null=True,
        blank=True,
        verbose_name="Tekstin väri EN",
    )

    description_fi = models.TextField(null=True, blank=True, verbose_name="Selite FI")
    description_sv = models.TextField(null=True, blank=True, verbose_name="Selite SV")
    description_en = models.TextField(null=True, blank=True, verbose_name="Selite EN")

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
            ],
            heading="Bannerin nimi",
            help_text="Otsikon maksimimerkkimäärä on noin 60 merkkiä sanojen pituudesta riippuen. Tarkistatathan esikatselusta, että sisältö on kooltaan sopiva.",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_background_image_fi"),
                ImageChooserPanel("hero_background_image_sv"),
                ImageChooserPanel("hero_background_image_en"),
            ],
            heading="Pääkuva",
            help_text="Pääkuvalla tarkoitetaan sivuston etusivulla olevaa koko sivun levyistä kuvaa.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("hero_background_image_color_fi"),
                FieldPanel("hero_background_image_color_sv"),
                FieldPanel("hero_background_image_color_en"),
            ],
            heading="Pääkuvan taustaväri",
            help_text="Pääkuvan taustalle tuleva väri.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("title_and_description_color_fi"),
                FieldPanel("title_and_description_color_sv"),
                FieldPanel("title_and_description_color_en"),
            ],
            heading="Tekstin Väri",
            help_text="",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_background_image_mobile_fi"),
                ImageChooserPanel("hero_background_image_mobile_sv"),
                ImageChooserPanel("hero_background_image_mobile_en"),
            ],
            heading="Pääkuva mobiililla",
            help_text="Pääkuvalla tarkoitetaan sivuston etusivulla olevaa koko sivun levyistä kuvaa. Tämä kuva näkyy vain mobiilissa.",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_top_layer_image_fi"),
                ImageChooserPanel("hero_top_layer_image_sv"),
                ImageChooserPanel("hero_top_layer_image_en"),
            ],
            heading="Pääkuvan päälle asettuva kuva",
            help_text="Kuva asettuu pääkuvan päälle. Tämä kuva ei näy mobiilissa. Ainoastaan taustakuva näkyy pienemmillä näytöillä.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("button_text_fi"),
                FieldPanel("button_text_sv"),
                FieldPanel("button_text_en"),
            ],
            heading="NAPPI",
            help_text="",
        ),
        MultiFieldPanel(
            [
                FieldPanel("button_url_fi"),
                FieldPanel("button_url_sv"),
                FieldPanel("button_url_en"),
            ],
            heading="NAPIN LINKKI",
            help_text="",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("social_media_image_fi"),
                ImageChooserPanel("social_media_image_sv"),
                ImageChooserPanel("social_media_image_en"),
            ],
            heading="Some-postauksen kuva",
            help_text="Kun käyttäjä jakaa etusivun somessa, tämä kuva tulee näkyviin postauksessa.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("title_fi"),
                FieldPanel("title_sv"),
                FieldPanel("title_en"),
            ],
            heading="OTSIKKO",
            help_text="Otsikon maksimimerkkimäärä on noin 60 merkkiä sanojen pituudesta riippuen. Tarkistatathan esikatselusta, että sisältö on kooltaan sopiva.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("description_fi"),
                FieldPanel("description_sv"),
                FieldPanel("description_en"),
            ],
            heading="SELITE",
            help_text="Selite sijoittuu otsikon yläpuolelle. Voit jättää tämän kohdan myös tyhjäksi.",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Sisältö"),
            ObjectList(
                CUSTOM_SETTINGS_PANELS, heading="Asetukset", classname="settings"
            ),
        ]
    )

    class Meta:
        verbose_name = "Banner"


class LandingPages(Page):
    parent_page_types = ["application.LandingPagesFolder"]
    subpage_typed = []

    top_banner = models.ForeignKey(
        BannerPages,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Top banner",
    )
    bottom_banner = models.ForeignKey(
        BannerPages,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Bottom banner",
    )

    meta_information_fi = models.TextField(null=True, verbose_name="Meta tieto FI")
    meta_information_sv = models.TextField(null=True, verbose_name="Meta tieto SV")
    meta_information_en = models.TextField(null=True, verbose_name="Meta tieto EN")

    page_title_fi = models.CharField(
        max_length=255, null=True, verbose_name="Sivun otsikointi FI"
    )
    page_title_sv = models.CharField(
        max_length=255, null=True, verbose_name="Sivun otsikointi SV"
    )
    page_title_en = models.CharField(
        max_length=255, null=True, verbose_name="Sivun otsikointi EN"
    )

    keywords_fi = StreamField(
        [
            ("keywords_fi", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords FI",
    )

    keywords_sv = StreamField(
        [
            ("keywords_sv", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords SV",
    )

    keywords_en = StreamField(
        [
            ("keywords_en", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords EN",
    )

    content_panels = [
        MultiFieldPanel(
            [PageChooserPanel("top_banner"), PageChooserPanel("bottom_banner")],
            heading="Banner selection",
            help_text="Pääkuvalla tarkoitetaan sivuston etusivulla olevaa koko sivun levyistä kuvaa.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("meta_information_fi"),
                FieldPanel("meta_information_sv"),
                FieldPanel("meta_information_en"),
            ],
            heading="META TIETO",
            help_text="Meta tieto avustaa hakukoneita tiedon etsimisessä.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("page_title_fi"),
                FieldPanel("page_title_sv"),
                FieldPanel("page_title_en"),
            ],
            heading="SIVUN OTSIKOINTI",
            help_text="",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("keywords_fi"),
                StreamFieldPanel("keywords_sv"),
                StreamFieldPanel("keywords_en"),
            ],
            heading="Keywords",
            help_text="",
        ),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["FRONTEND_BASE_URL"] = settings.FRONTEND_BASE_URL
        return context

    def clean(self):
        """
        Unfortunately Wagtail doesn't support customizing which field it uses for Page titles.
        At the moment, it uses "title" field, but this is not always desirable.
        The extremely hacky trick below makes Wagtail explorer look like its default language is Finnish.
        Taken from: https://stackoverflow.com/a/48632873/5208999
        """
        self.title = (
            self.top_banner and self.top_banner.title_fi
        ) or "Etusivu ilman suomenkielistä otsikkoa"
        self.slug = str(uuid4())
        super().clean()

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Sisältö"),
            ObjectList(
                CUSTOM_SETTINGS_PANELS, heading="Asetukset", classname="settings"
            ),
        ]
    )

    class Meta:
        verbose_name = "Landing Page"


class Collections(Page):
    parent_page_types = ["application.CollectionsFolder"]
    subpage_typed = []
    color_choices = [
        ("ENGEL", "Engel – keltainen"),
        ("COPPER", "Kupari – vihreä"),
        ("SUOMENLINNA", "Suomenlinna – vaaleanpunainen"),
    ]

    visible_on_frontpage = models.BooleanField(
        default=False, verbose_name="Näytä kokoelma etusivulla"
    )
    hero_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Kokoelman pääkuva",
    )
    box_color = models.CharField(
        max_length=255,
        choices=color_choices,
        null=True,
        verbose_name="Taustaväri ylätunnisteelle",
    )

    title_fi = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Otsikko FI"
    )
    title_sv = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Otsikko SV"
    )
    title_en = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Otsikko EN"
    )

    description_fi = models.TextField(
        max_length=700, null=True, blank=True, verbose_name="Kuvaus FI"
    )
    description_sv = models.TextField(
        max_length=700, null=True, blank=True, verbose_name="Kuvaus SV"
    )
    description_en = models.TextField(
        max_length=700, null=True, blank=True, verbose_name="Kuvaus EN"
    )

    link_text_fi = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Linkki teksti FI"
    )
    link_text_sv = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Linkki teksti SV"
    )
    link_text_en = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Linkki teksti EN"
    )

    link_url_fi = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Linkki suomenkieliselle sivulle",
    )
    link_url_sv = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Linkki ruotsinkieliselle sivulle",
    )
    link_url_en = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Linkki englanninkieliselle sivulle",
    )

    social_media_description_fi = models.TextField(
        null=True, blank=True, verbose_name="Some-kuvaus FI"
    )
    social_media_description_sv = models.TextField(
        null=True, blank=True, verbose_name="Some-kuvaus SV"
    )
    social_media_description_en = models.TextField(
        null=True, blank=True, verbose_name="Some-kuvaus EN"
    )

    curated_events_title_fi = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Tapahtumien otsikko FI",
        default="Suositellut tapahtumat",
    )
    curated_events_title_sv = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Tapahtumien otsikko SV",
        default="Rekommenderade evenemang",
    )
    curated_events_title_en = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Tapahtumien otsikko EN",
        default="Recommended events",
    )

    curated_events = StreamField(
        [
            ("event_link", blocks.URLBlock()),
        ],
        null=True,
        verbose_name="Suositeltavat tapahtumat",
    )

    event_list_title_fi = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Tapahtumien otsikko FI",
        default="Sinua voisi myös kiinnostaa",
    )
    event_list_title_sv = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Tapahtumien otsikko SV",
        default="Kolla även dessa",
    )
    event_list_title_en = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Tapahtumien otsikko EN",
        default="Related events",
    )

    event_list_query_fi = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Hakutulossivun www-osoite FI",
    )
    event_list_query_sv = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Hakutulossivun www-osoite SV",
    )
    event_list_query_en = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Hakutulossivun www-osoite EN",
    )

    course_list_query_fi = models.URLField(
        max_length=500, null=True, blank=True, verbose_name="Course List Query FI"
    )
    course_list_query_sv = models.URLField(
        max_length=500, null=True, blank=True, verbose_name="Course List Query SV"
    )
    course_list_query_en = models.URLField(
        max_length=500, null=True, blank=True, verbose_name="Course List Query EN"
    )

    keywords_fi = StreamField(
        [
            ("keywords_fi", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords FI",
    )

    keywords_sv = StreamField(
        [
            ("keywords_sv", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords SV",
    )

    keywords_en = StreamField(
        [
            ("keywords_en", blocks.CharBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="keywords EN",
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
            ],
            heading="Lyhytnimi",
            help_text="Lyhytnimi määrittelee sivun nimen esiintymisen URL:eissa esim. http://domain.com/blog/[polkutunnus]/",
        ),
        MultiFieldPanel(
            [
                FieldPanel("visible_on_frontpage"),
            ],
            heading="Näytä kokoelma etusivulla",
            help_text='Valitessasi "Näytä kokoelma etusivulla" kokoelma tulee näkyviin kokoelmasivun lisäksi myös palvelun etusivulla.',
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("hero_image"),
            ],
            heading="Kokoelman pääkuva",
            help_text="Kuvan maksimikoko on 200 KB. Kuvan tulisi olla vähintään 970 px leveä ja 650 px korkea.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("box_color"),
            ],
            heading="Taustaväri ylätunnisteelle",
            help_text="Valittu väri tulee näkyviin kokoelman yläosaan, joka sisältää kokoelman otsikon sekä kuvauksen.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("title_fi"),
                FieldPanel("title_sv"),
                FieldPanel("title_en"),
            ],
            heading="OTSIKKO",
            help_text="Kokoelma julkaistaan vain niillä kielillä, joilla on otsikko. Voit halutessasi jättää otsikkokentän tyhjäksi, jolloin kyseistä kieliversiota ei julkaista.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("description_fi"),
                FieldPanel("description_sv"),
                FieldPanel("description_en"),
            ],
            heading="KOKOELMAN KUVAUS",
            help_text="Pääotsikon alle tuleva teksti, joka kertoo lisää kokoelmasta ja houkuttelee käyttäjiä tutustumaan suosituksiin. Kuvauksen maksimimerkkimäärä on 400 merkkiä.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("link_text_fi"),
                FieldPanel("link_text_sv"),
                FieldPanel("link_text_en"),
            ],
            heading="Linkkiteksti - valinnainen",
            help_text="Vapaaehtoinen linkki, joka ohjaa lukijan pois kokoelmasta. Käytä vain harkitusti ja pidä linkkiteksti lyhyenä.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("link_url_fi"),
                FieldPanel("link_url_sv"),
                FieldPanel("link_url_en"),
            ],
            heading="Linkin www-osoite - valinnainen",
            help_text="Jos lisäsit aikaisempaan 'Linkkiteksti'-osioon linkin, lisää tähän kenttään www-osoite, johon käyttäjä ohjataan.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("curated_events_title_fi"),
                FieldPanel("curated_events_title_sv"),
                FieldPanel("curated_events_title_en"),
            ],
            heading="Nostojen otsikko",
            help_text="Kirjoita tähän otsikko, jonka haluat näyttää käsin poimittavien, suositeltavien tapahtumien yläpuolella.",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("curated_events"),
            ],
            heading="SUOSITELTAVAT TAPAHTUMAT",
            help_text="Lisää tähän ne tapahtumat, joita haluat suositella käyttäjälle. Tapahtumat näkyvät siinä järjestyksessä, jossa syötät ne. Voit helposti lisätä uusia tapahtumia, poistaa niitä ja muuttaa järjestystä. Mene haluamasi tapahtuman sivulle, kopioi sen www-osoite ja liitä osoite alla olevaan kenttään.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("event_list_title_fi"),
                FieldPanel("event_list_title_sv"),
                FieldPanel("event_list_title_en"),
            ],
            heading="MUIDEN TAPAHTUMIEN OTSIKKO",
            help_text='Käsin poimittujen tapahtumien voit tässä suositella muita samankaltaisia tai muuten kiinnostavia tapahtumia. Näille tapahtumille tarvitaan oma otsikko, esim. "Tutustu myös näihin".',
        ),
        MultiFieldPanel(
            [
                FieldPanel("event_list_query_fi"),
                FieldPanel("event_list_query_sv"),
                FieldPanel("event_list_query_en"),
            ],
            heading="TAPAHTUMALISTAUKSEN HAUN WWW-OSOITE",
            help_text="Tee tapahtumahaku sopivilla hakukriteereillä tapahtumat.helsingissa. Kun hakutuloksessa on haluamasi tapahtumat, kopioi hakutuloksen www-osoite tähän kenttään.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("course_list_query_fi"),
                FieldPanel("course_list_query_sv"),
                FieldPanel("course_list_query_en"),
            ],
            heading="Course List Query",
            help_text="",
        ),
        MultiFieldPanel(
            [
                FieldPanel("social_media_description_fi"),
                FieldPanel("social_media_description_sv"),
                FieldPanel("social_media_description_en"),
            ],
            heading="KUVAUS SOSIAALISEEN MEDIAAN",
            help_text="Tämä teksti näkyy, kun käyttäjä jakaa kokoelman sosiaalisessa mediassa. Max. 160 merkkiä pitkä teksti, joka houkuttelee avaamaan linkin.",
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel("keywords_fi"),
                StreamFieldPanel("keywords_sv"),
                StreamFieldPanel("keywords_en"),
            ],
            heading="Keywords",
            help_text="",
        ),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["FRONTEND_BASE_URL"] = settings.FRONTEND_BASE_URL
        return context

    def clean(self):
        """
        Unfortunately Wagtail doesn't support customizing which field it uses for Page titles.
        At the moment, it uses "title" field, but this is not always desirable.
        The extremely hacky trick below makes Wagtail explorer look like its default language is Finnish.
        Taken from: https://stackoverflow.com/a/48632873/5208999
        """
        self.title = self.title_fi or "Kokoelma ilman suomenkielistä otsikkoa"
        super().clean()

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Sisältö"),
            ObjectList(
                CUSTOM_SETTINGS_PANELS, heading="Asetukset", classname="settings"
            ),
        ]
    )

    class Meta:
        verbose_name = "Collection"
