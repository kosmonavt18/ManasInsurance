from django.urls import path
from . import views

app_name = 'auto'
urlpatterns = [
    path('', views.AutoListView.as_view(), name='list'),
    path('<slug:slug>/', views.AutoDetailView.as_view(), name='detail'),
]
