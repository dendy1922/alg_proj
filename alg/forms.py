from django import forms
from .models import Algorithm_description


class AlgForm(forms.Form):
    """
    Form for picking sorting method and uploading file
    """

    algorithms = forms.ChoiceField(
        choices=[(c.name, c.name) for c in Algorithm_description.objects.all()],
    )
    file = forms.FileField()