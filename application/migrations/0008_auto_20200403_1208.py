# Generated by Django 2.2.9 on 2020-04-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_landingpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='event_list_query',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_url_en',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_url_fi',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_url_sv',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_url_en',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_url_fi',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_url_sv',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
