from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import ContactView
from .views import ProductIndexView, ProductShowView


urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'), 
path('products/<str:id>', ProductShowView.as_view(), name='show')
]