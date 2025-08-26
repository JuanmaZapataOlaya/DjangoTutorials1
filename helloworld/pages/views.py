from django.shortcuts import render # here by default 
from django.views.generic import TemplateView 
from django.views import View
from django.http import HttpResponseRedirect  # Agrega esta importación
from django import forms 
from django.shortcuts import redirect 


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Your Name", 
        }) 
 
        return context

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price": 1000}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 2000}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"," price": 3000}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 4000}, 
    ] 
 
class ProductIndexView(View): 
    template_name = 'products/index.html' 
 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'products/show.html' 
 
    def get(self, request, id): 
        # Validar si el id es un número válido y existe el producto
        try:
            idx = int(id) - 1
            if idx < 0 or idx >= len(Product.products):
                return HttpResponseRedirect('/')  # Redirige a home si no es válido
            product = Product.products[idx]
        except (ValueError, IndexError):
            return HttpResponseRedirect('/')  # Redirige a home si hay error

        viewData = {} 
        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] =  product["name"] + " - Product information" 
        viewData["product"] = product 
 
        return render(request, self.template_name, viewData)

    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 
 
 
class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("The price must be greater than zero.")
        return price
 
class ProductCreateView(View): 
    template_name = 'products/create.html' 
 
    def get(self, request): 
        form = ProductForm()
        return render(request, self.template_name, {"title": "Create product", "form": form})
 
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return render(request, 'products/created.html', {"title": "Product created"})
        # Si el formulario no es válido, vuelve a mostrar el formulario con errores
        return render(request, self.template_name, {"title": "Create product", "form": form})