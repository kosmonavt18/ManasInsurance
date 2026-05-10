from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.ClientProductListView.as_view(), name='list'),
    path('<slug:slug>/', views.ClientProductDetailView.as_view(), name='detail'),
]
