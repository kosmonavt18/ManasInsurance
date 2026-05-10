from django.urls import path
from . import views

app_name = 'corporate'
urlpatterns = [
    path('', views.CorporateListView.as_view(), name='list'),
    path('<slug:slug>/', views.CorporateDetailView.as_view(), name='detail'),
]
