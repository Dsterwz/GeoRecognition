from django import forms
from core.models import TempImage


class ImageForm(forms.ModelForm):

    class Meta:
        model = TempImage
        fields = [
            "image",
        ]