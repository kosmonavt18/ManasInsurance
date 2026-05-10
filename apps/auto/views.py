from django.views.generic import ListView, DetailView
from .models import AutoProduct


class AutoListView(ListView):
    template_name = 'auto/list.html'
    model = AutoProduct
    context_object_name = 'products'
    queryset = AutoProduct.objects.filter(is_active=True)


class AutoDetailView(DetailView):
    template_name = 'auto/detail.html'
    model = AutoProduct
    context_object_name = 'product'
