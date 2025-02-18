from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import Product
from .forms import ProductModelForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'home.html'


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        # Obtém o contexto padrão
        context = super().get_context_data(**kwargs)

        # Adiciona os produtos e sua contagem
        products = Product.objects.all()
        products_count = products.count()
        context['products'] = products
        context['products_count'] = products_count
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('dashboard')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('dashboard')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

