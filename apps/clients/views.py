from django.views.generic import ListView, DetailView
from .models import ClientProduct


class ClientProductListView(ListView):
    template_name = 'clients/list.html'
    model = ClientProduct
    context_object_name = 'products'
    queryset = ClientProduct.objects.filter(is_active=True)


class ClientProductDetailView(DetailView):
    template_name = 'clients/detail.html'
    model = ClientProduct
    context_object_name = 'product'
