# Generated by Django 2.2.9 on 2020-03-16 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20200316_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collections',
            old_name='short_description_en',
            new_name='subtitles_en',
        ),
        migrations.RenameField(
            model_name='collections',
            old_name='short_description_fi',
            new_name='subtitles_fi',
        ),
        migrations.RenameField(
            model_name='collections',
            old_name='short_description_sv',
            new_name='subtitles_sv',
        ),
    ]
