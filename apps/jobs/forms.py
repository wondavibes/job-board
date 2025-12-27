from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["company", "title", "description", "location"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user and user.role == "employer":
            # Limit companies to those owned by this employer
            self.fields["company"].queryset = user.company_set.all()
