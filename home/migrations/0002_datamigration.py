# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 12:16
from __future__ import unicode_literals

from django.db import migrations


def prettify_site(apps, schema_editor):
    Site = apps.get_model('wagtailcore', 'Site')
    Page = apps.get_model('wagtailcore', 'Page')
    site = Site.objects.get(is_default_site=True)
    page = Page.objects.get(sites_rooted_here=True)
    site.hostname = '127.0.0.1'
    site.port = 8000
    site.site_name = 'Лендинг'
    site.save()
    page.title = 'Главная'
    page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            prettify_site, reverse_code=migrations.RunPython.noop),
    ]
