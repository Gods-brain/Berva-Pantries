from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Products, Bundles
import random
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class Home(ListView):
    model = Products
    template_name = 'shop/home.html'
    context_object_name = 'product'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bundles = list(Bundles.objects.all())  # convert to list for random functions

        # show 2 bundles ONLY if there are up to 2
        if len(bundles) >= 2:
            context['bundles'] = random.sample(bundles, 2)
        else:
            context['bundles'] = bundles  # show whatever is available

        # weekly bundle (one random bundle)
        if bundles:
            context['weekbundle'] = random.choice(bundles)
        else:
            context['weekbundle'] = None

        return context


class Detail(DetailView):
    model = Products
    template_name = 'shop/detail.html'
    context_object_name = 'product'

class BundleDetail(DetailView):
    model = Bundles
    template_name = 'shop/detail.html'
    context_object_name = 'product'

class SearchResult(ListView):
    template_name = "shop/search.html"
    context_object_name = "result"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        products = Products.objects.filter(Q(name__icontains=query))
        bundles = Bundles.objects.filter(Q(name__icontains=query))
        combined_results = list(products) + list(bundles)
        return combined_results


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['product_num'] = len(self.get_queryset())
        return context

class BundleResult(ListView):
    model = Bundles
    template_name = "shop/search.html"
    context_object_name = "result"
    paginate_by = 10
