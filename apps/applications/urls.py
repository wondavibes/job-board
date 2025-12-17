from django.urls import path
from .views import ApplyToJobView

urlpatterns = [
    path("apply/<int:job_id>/", ApplyToJobView.as_view(), name="apply_to_job"),
]
