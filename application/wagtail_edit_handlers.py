from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.widgets import AdminImageChooser


class CustomImageChooserPanel(ImageChooserPanel):
    def widget_overrides(self):
        return {self.field_name: AdminImageChooser(show_edit_link=False)}
