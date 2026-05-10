from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('cases/', views.InsuranceCasesView.as_view(), name='cases'),
    path('cases/<str:category>/', views.InsuranceCaseDetailView.as_view(), name='case_detail'),
]
