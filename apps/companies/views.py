from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyForm
from apps.accounts.mixins import EmployerRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from typing import cast


class CompanyCreateView(EmployerRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "companies/company_form.html"
    success_url = reverse_lazy("employer_dashboard")

    def form_valid(self, form):
        # Attach the logged-in employer as the owner
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CompanyUpdateView(EmployerRequiredMixin, UpdateView):
    model = Company
    fields = ["name", "industry", "location", "website", "description"]
    template_name = "companies/company_form.html"
    success_url = reverse_lazy("employer_dashboard")

    def get_queryset(self):
        # Only allow editing of the employer’s own companies

        return Company.objects.filter(owner=self.request.user)


class CompanyDeleteView(EmployerRequiredMixin, DeleteView):
    model = Company
    template_name = "companies/company_delete.html"
    success_url = reverse_lazy("employer_dashboard")

    def get_queryset(self):
        # Only allow editing of the employer’s own companies

        return Company.objects.filter(owner=self.request.user)
