from django import forms
from .models import Alg


class AlgForm(forms.Form):

    algorithms = forms.ChoiceField(
        choices=[(c.name, c.name) for c in Alg.objects.all()],
    )
    file = forms.FileField()