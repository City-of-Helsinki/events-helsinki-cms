from wagtail.admin.edit_handlers import PublishingPanel, PrivacyModalPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.widgets import AdminImageChooser


class CustomImageChooserPanel(ImageChooserPanel):
    def widget_overrides(self):
        return {self.field_name: AdminImageChooser(show_edit_link=False)}


CUSTOM_SETTINGS_PANELS = [
    PublishingPanel(help_text='Sekä julkaisu- että poistopäivämäärä ovat vapaaehtoisia kenttiä ja '
                    'ne voidaan jättää tyhjäksi. Voit myös halutessasi täyttää vain toisen kentistä.'),
    PrivacyModalPanel(help_text='Tällä voit määritellä sivun ja sen alasivujen näkyvyyden.'),
]
