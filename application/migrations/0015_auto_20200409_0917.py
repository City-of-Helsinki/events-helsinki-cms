# Generated by Django 2.2.9 on 2020-04-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_auto_20200408_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='event_list_query',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Hakutulossivun www-osoite'),
        ),
    ]
