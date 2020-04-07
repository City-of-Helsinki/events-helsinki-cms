# Generated by Django 2.2.9 on 2020-04-07 17:19

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20200407_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='curated_events',
            field=wagtail.core.fields.StreamField([('event_link', wagtail.core.blocks.URLBlock())], null=True, verbose_name='Suositeltavat tapahtumat'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='curated_events_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tapahtumien otsikko EN'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='curated_events_title_fi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tapahtumien otsikko FI'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='curated_events_title_sv',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tapahtumien otsikko SV'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Kuvaus EN'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='description_fi',
            field=models.TextField(blank=True, null=True, verbose_name='Kuvaus FI'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='description_sv',
            field=models.TextField(blank=True, null=True, verbose_name='Kuvaus SV'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='event_list_query',
            field=models.URLField(max_length=500, null=True, verbose_name='Hakutulossivun www-osoite'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='event_list_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tapahtumien otsikko EN'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='event_list_title_fi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tapahtumien otsikko FI'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='event_list_title_sv',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tapahtumien otsikko SV'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_text_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Linkki teskti EN'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_text_fi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Linkki teskti FI'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_text_sv',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Linkki teskti SV'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_url_en',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Linkki englanninkieliselle sivulle'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_url_fi',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Linkki suomenkieliselle sivulle'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='link_url_sv',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Linkki ruotsinkieliselle sivulle'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='social_media_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Some-kuvaus EN'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='social_media_description_fi',
            field=models.TextField(blank=True, null=True, verbose_name='Some-kuvaus FI'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='social_media_description_sv',
            field=models.TextField(blank=True, null=True, verbose_name='Some-kuvaus SV'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='title_fi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Otsikko FI'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='title_sv',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Otsikko SV'),
        ),
    ]
