from django.urls import path
from .views import (
    job_list_view,
    job_detail_view,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
)

urlpatterns = [
    path("", job_list_view, name="job_list"),
    path("<int:job_id>/", job_detail_view, name="job_detail"),
    path("create/", JobCreateView.as_view(), name="job_create"),
    path("<int:pk>/update/", JobUpdateView.as_view(), name="job_update"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
]
