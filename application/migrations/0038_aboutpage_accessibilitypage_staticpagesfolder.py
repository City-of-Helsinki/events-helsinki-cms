# Generated by Django 2.2.9 on 2020-09-11 15:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('application', '0037_customimage_photographer_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading_section_fi', wagtail.core.fields.RichTextField()),
                ('heading_section_sv', wagtail.core.fields.RichTextField()),
                ('heading_section_en', wagtail.core.fields.RichTextField()),
                ('content_section_fi', wagtail.core.fields.RichTextField()),
                ('content_section_sv', wagtail.core.fields.RichTextField()),
                ('content_section_en', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'About Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AccessibilityPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading_section_fi', wagtail.core.fields.RichTextField()),
                ('heading_section_sv', wagtail.core.fields.RichTextField()),
                ('heading_section_en', wagtail.core.fields.RichTextField()),
                ('content_section_fi', wagtail.core.fields.RichTextField()),
                ('content_section_sv', wagtail.core.fields.RichTextField()),
                ('content_section_en', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Accessibility Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StaticPagesFolder',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Static Pages Folder',
            },
            bases=('wagtailcore.page',),
        ),
    ]
