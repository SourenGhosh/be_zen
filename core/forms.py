from django import forms
from core.models import MediaConverter



class MediaConverterForm(forms.ModelForm):
    class Meta:
        model=MediaConverter
        fields=[
            "name",
            "attachment",
        ]