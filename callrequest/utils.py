from __future__ import unicode_literals, absolute_import

import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.mail import get_connection
from django.template.loader import render_to_string

from home.models import ThisSiteSettings

DEFAULT_MANAGER_EMAIL = [
    os.environ.get('MANAGER_EMAIL', 'manager@example.com')]
BAD_FIELDS = ['ID', 'id', 'edited_at', 'ipaddress', 'source']


def to_dict(instance):
    opts = instance._meta
    data = {}
    for field in opts.concrete_fields:
        if field.name not in BAD_FIELDS:
            data[field.verbose_name] = field.value_from_object(instance)
    return data


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_callrequest(instance, site, subject, to):
    site_settings = ThisSiteSettings.for_site(site)
    site_domain = site.hostname
    from_email = site_settings.from_email or settings.FROM_EMAIL

    base_context = {'object': instance, 'site_domain': site_domain}
    base_context['subject'] = 'Спасибо за заявку на сайте {}'.format(site_domain)
    client_context = base_context
    base_context['subject'] = 'Новая заявка на сайте {}'.format(site_domain)
    manager_context = base_context

    managers_emails = list(
        User.objects.filter(
            groups__name__contains="callrequest").values_list(
            'email', flat=True))

    client_msg = prepare_email(
        client_context, [to] or [instance.email], from_email)
    managers_msg = prepare_email(
        manager_context, managers_emails or DEFAULT_MANAGER_EMAIL,
        from_email)

    connection = get_connection()
    connection.open()
    connection.send_messages([client_msg, managers_msg])
    connection.close()


def prepare_email(context, recipients, from_email):
    text_content = render_to_string(
        'callrequest/email/content.txt', context)
    html_content = render_to_string(
        'callrequest/email/content.html', context)

    msg = EmailMultiAlternatives(
        subject=context['subject'], body=text_content,
        from_email=from_email, to=recipients)
    msg.attach_alternative(html_content, 'text/html')
    return msg
