from __future__ import absolute_import, unicode_literals

from django import forms

from .models import CallRequest


class CallRequestForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(CallRequestForm, self).clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if not (email or phone):
            raise forms.ValidationError(
                'Хотя бы одно поле должно быть заполнено')

    class Meta:
        fields = ["name", "phone", "email", "comment", "source"]
        model = CallRequest


class CallRequestPhoneForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'phone']
        model = CallRequest


class CallRequestEmailForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'email']
        model = CallRequest
