from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import BaseCallRequestView


urlpatterns = [
    url(r'new/$', csrf_exempt(BaseCallRequestView.as_view()), name='new'),
]
