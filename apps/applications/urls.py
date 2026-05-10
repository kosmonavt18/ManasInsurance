from django.urls import path
from . import views

app_name = 'applications'
urlpatterns = [
    path('new/', views.ApplicationCreateView.as_view(), name='create'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]
