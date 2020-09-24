from django.utils.translation import gettext

'''
https://github.com/wagtail/wagtail/blob/master/wagtail/admin/locale/fi/LC_MESSAGES/django.po

To overwrite what Wagtail shows for default translated Finnish texts:

1. We must *mark* the message we would like to overwrite in this module using gettext
2. We must *update* the Finnish locale file with the message we marked using: django-admin makemessages --locale fi
3. We must *provide* our own desired translation in the Finnish locale file in locale/fi/LC_MESSAGES/django.po
4. We must *compile* the Finnish locale file using: django-admin compilemessages
'''
gettext("The page could not be saved due to validation errors")
gettext("Upload")
gettext("Uploading…")
gettext("Set page privacy")
