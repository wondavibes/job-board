from django.urls import path
from .views import (
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
)

urlpatterns = [
    path("create/", CompanyCreateView.as_view(), name="company_create"),
    path("<int:pk>/update/", CompanyUpdateView.as_view(), name="company_update"),
    path("<int:pk>/delete/", CompanyDeleteView.as_view(), name="company_delete"),
]
