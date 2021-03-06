# Generated by Django 2.2.9 on 2020-06-15 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('application', '0027_auto_20200511_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpages',
            name='social_media_image_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='landingpages',
            name='social_media_image_fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='landingpages',
            name='social_media_image_sv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
    ]
