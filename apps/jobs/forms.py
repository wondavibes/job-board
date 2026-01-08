from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user and user.role == "employer":
            # Limit companies to those owned by this employer
            self.fields["company"].queryset = user.companies.all()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if self.user and title and description:
            exists = Job.objects.filter(
                company=self.user.company,
                title=title,
                description=description,
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "A job with the same title and description already exists for your company."
                )

        return cleaned_data
