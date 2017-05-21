from __future__ import absolute_import, unicode_literals

from django.db import models


class BaseCallRequest(models.Model):

    created_at = models.DateTimeField(
        'Создано', auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    ipaddress = models.GenericIPAddressField(
        null=True, blank=True, editable=False)
    source = models.CharField(
        'Источник обращения', max_length=255,
        blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ('-created_at', )


class CallRequest(BaseCallRequest):
    name = models.CharField(
        'Имя', max_length=255, null=True, blank=True)
    phone = models.CharField(
        'Телефон', max_length=255, null=True, blank=True)
    email = models.CharField(
        'E-mail', max_length=255, null=True, blank=True)
    company = models.CharField(
        'Компания', max_length=255, null=True, blank=True)

    comment = models.TextField('Сообщение', blank=True, null=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Обратная связь'
