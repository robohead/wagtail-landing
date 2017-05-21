from __future__ import absolute_import, unicode_literals

from django.http import JsonResponse
from django.views.generic import View

from .forms import CallRequestForm

from .utils import get_client_ip
from .utils import send_callrequest
from .utils import to_dict


class BaseCallRequestView(View):
    form_class = CallRequestForm
    subject = 'Новая заявка на обратную связь'
    to = None
    initial = {}

    def post(self, request):
        form = self.form_class(request.POST, initial=self.initial)
        if form.is_valid():
            callrequest = form.save()
            try:
                callrequest.ipaddress = get_client_ip(request)
                callrequest.save()
            except Exception:
                pass
            send_callrequest(
                to_dict(callrequest), site=request.site,
                subject=self.subject, to=self.to)
        return JsonResponse({
            'result': 'fail' if form.errors else 'success',
            'errors': form.errors or ''})
