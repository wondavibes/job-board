from django.urls import path
from .views import ApplyToJobView, JobApplicantsView

urlpatterns = [
    path("apply/<int:job_id>/", ApplyToJobView.as_view(), name="apply_to_job"),
    path(
        "jobs/<int:job_id>/applicants/",
        JobApplicantsView.as_view(),
        name="job_applicants",
    ),
]
