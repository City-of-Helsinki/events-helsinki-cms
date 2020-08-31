# Generated by Django 2.2.9 on 2020-08-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0034_auto_20200806_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_color_en',
            field=models.CharField(blank=True, choices=[('FOG', 'Sumu'), ('ENGEL', 'Engel'), ('COPPER', 'Kupari'), ('SUOMENLINNA', 'Suomenlinna')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_color_fi',
            field=models.CharField(blank=True, choices=[('FOG', 'Sumu'), ('ENGEL', 'Engel'), ('COPPER', 'Kupari'), ('SUOMENLINNA', 'Suomenlinna')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_color_sv',
            field=models.CharField(blank=True, choices=[('FOG', 'Sumu'), ('ENGEL', 'Engel'), ('COPPER', 'Kupari'), ('SUOMENLINNA', 'Suomenlinna')], max_length=255, null=True),
        ),
    ]