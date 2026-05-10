from django.urls import path
from . import views

app_name = 'calculators'
urlpatterns = [
    path('', views.CalculatorsIndexView.as_view(), name='index'),
    path('osago/', views.OSAGOCalculatorView.as_view(), name='osago'),
    path('kasko/', views.KASKOCalculatorView.as_view(), name='kasko'),
    path('property/', views.PropertyCalculatorView.as_view(), name='property'),
    path('travel/', views.TravelCalculatorView.as_view(), name='travel'),
]
