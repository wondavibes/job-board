from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    website = forms.URLField(
        required=False,
        assume_scheme="https",
        # Using TextInput bypasses the browser's strict <input type="url"> check
        widget=forms.TextInput(
            attrs={
                "placeholder": "www.example.com",
                "class": "w-full p-2 border rounded",  # Example Tailwind classes
            }
        ),
    )

    class Meta:
        model = Company
        # Listing fields explicitly is safer than "__all__"
        fields = ["name", "industry", "description", "location", "website"]
