from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyForm
from accounts.mixins import EmployerRequiredMixin


class CompanyCreateView(EmployerRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "companies/company_form.html"
    success_url = reverse_lazy("employer_dashboard")

    def form_valid(self, form):
        # Attach the logged-in employer as the owner
        form.instance.owner = self.request.user
        return super().form_valid(form)
