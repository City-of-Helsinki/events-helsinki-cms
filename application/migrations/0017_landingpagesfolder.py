# Generated by Django 2.2.9 on 2020-04-09 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('application', '0016_auto_20200409_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPagesFolder',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Landing Pages Folder',
            },
            bases=('wagtailcore.page',),
        ),
    ]
