from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

    def clean_website(self):
        website = self.cleaned_data.get("website")

        if website and not website.startswith(("http://", "https://")):
            website = "https://" + website

        return website
