from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    sort = request.GET.get('sort')
    phones_obj = Phone.objects.all()
    context['phones'] = phones_obj

    if sort == 'name':
        phones_obj = Phone.objects.order_by('name')
        context['phones'] = phones_obj
    elif sort == 'min_price':
        phones_obj = Phone.objects.order_by('price')
        context['phones'] = phones_obj
    elif sort == 'max_price':
        phones_obj = Phone.objects.order_by('-price')
        context['phones'] = phones_obj

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phones_list = Phone.object.get(slug=slug)
    context['phones'] = phones_list
    return render(request, template, context)