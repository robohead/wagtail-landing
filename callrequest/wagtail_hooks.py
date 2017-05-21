from __future__ import absolute_import, unicode_literals

from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail.contrib.modeladmin.options import modeladmin_register

from .models import CallRequest


class CallRequestModelAdmin(ModelAdmin):
    model = CallRequest
    menu_icon = 'mail'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = True
    inspect_view_enabled = True
    list_display = ('name', 'email', 'phone', 'ipaddress')
    search_fields = ('name', 'email', 'phone', 'ipaddress')
    form_fields_exclude = ('source', )


modeladmin_register(CallRequestModelAdmin)
