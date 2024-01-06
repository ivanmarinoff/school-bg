from django import forms
from django import template

from school_bg.web.models import WEBContent

register = template.Library()


class WEBContentForm(forms.ModelForm):
    class Meta:
        model = WEBContent
        fields = '__all__'


class WEBContentReadForm(WEBContentForm):
    pass

