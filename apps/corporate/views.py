from django.views.generic import ListView, DetailView
from .models import CorporateProduct


class CorporateListView(ListView):
    template_name = 'corporate/list.html'
    model = CorporateProduct
    context_object_name = 'products'
    queryset = CorporateProduct.objects.filter(is_active=True)


class CorporateDetailView(DetailView):
    template_name = 'corporate/detail.html'
    model = CorporateProduct
    context_object_name = 'product'
