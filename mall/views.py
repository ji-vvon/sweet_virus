from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class ProductList(ListView):
    model = Product
    ordering = '-pk'


class ProductDetail(DetailView):
    model = Product