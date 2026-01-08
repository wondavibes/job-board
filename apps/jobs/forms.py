# forms.py
from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # Ensure these are not in the form fields
        exclude = ["company", "employer"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        # Validation for duplicate jobs within the same company
        if self.user and hasattr(self.user, "company") and title and description:
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
