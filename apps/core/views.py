from django.views.generic import TemplateView, ListView, DetailView
from .models import InsuranceCase, Branch
from apps.clients.models import ClientProduct
from apps.corporate.models import CorporateProduct
from apps.auto.models import AutoProduct


class HomeView(TemplateView):
    """Главная страница."""
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['client_products'] = ClientProduct.objects.filter(is_active=True)[:3]
        ctx['corporate_products'] = CorporateProduct.objects.filter(is_active=True)[:3]
        ctx['auto_products'] = AutoProduct.objects.filter(is_active=True)[:4]
        return ctx


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactsView(ListView):
    template_name = 'core/contacts.html'
    model = Branch
    context_object_name = 'branches'


class InsuranceCasesView(ListView):
    template_name = 'core/cases_list.html'
    model = InsuranceCase
    context_object_name = 'cases'


class InsuranceCaseDetailView(DetailView):
    template_name = 'core/case_detail.html'
    model = InsuranceCase
    slug_field = 'category'
    slug_url_kwarg = 'category'
    context_object_name = 'case'
