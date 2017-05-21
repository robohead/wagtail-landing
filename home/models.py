from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.api import APIField
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.models import register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock


@register_setting(icon='home')
class ThisSiteSettings(BaseSetting):
    phone = models.CharField(
        'Основной номер телефона', default='911',
        max_length=20)
    email = models.EmailField(
        'Основной email', default='hello@example.com')
    address = models.TextField(
        'Основной адрес', default='Moscow, Tolstoy square')
    from_email = models.EmailField(
        'Адрес отправителя', default='robot@example.com',
        help_text='Email-адрес с которого приходят письма.')

    class Meta:
        verbose_name = 'Основные'


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    api_fields = [
        APIField('body'),
    ]

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
