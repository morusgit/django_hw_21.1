from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Contact


def index(request):
    product_list = Product.objects.all().order_by('pk')
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        'title': 'Каталог товаров'
    }
    return render(request, 'catalog/index.html', context)


def show_item(request, product_pk):
    item = get_object_or_404(Product, pk=product_pk)
    context = {
        'item': item,
        'title': item
    }
    return render(request, 'catalog/item.html', context)


class ProductList(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/item.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['item'] = item
        context_data['title'] = item
        return context_data


#class ContactsView(ListView):
#    model = Contact
#    template_name = 'catalog/contacts.html'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты!',
    }

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name: {name}, email: {email}, message: {message}')
        return render(request, 'catalog/contacts.html', self.extra_context)