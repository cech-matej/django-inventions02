import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

import random

from inventions.models import Invention, Inventor, Category, Nation
from inventions.forms import InventionModelForm


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_inventions = Invention.objects.all().count()
    inventions = Invention.objects.order_by('-date_of_invention')

    inventions_to_random = list(Invention.objects.all())
    random_invention = random.choice(inventions_to_random)

    context = {
        'num_inventions': num_inventions,
        'inventions': inventions,
        'random_invention': random_invention
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def statistics(request):
    # POČET VYNÁLEZCŮ V ZEMI
    nations_all = Nation.objects.all()
    nations = []

    for nation in nations_all:
        nations.append(nation.abbr)

    inventors = Inventor.objects.all()
    inventors_num = []

    for nation in nations:
        inventors_num.append(inventors.filter(nation_id__abbr=nation).count())

    # POČET VYNÁLEZŮ V KATEGORII
    categories_all = Category.objects.all()
    categories = []

    for category in categories_all:
        categories.append(category.name)

    inventions = Invention.objects.all()
    inventions_num = []

    for category in categories:
        inventions_num.append(inventions.filter(category__name=category).count())

    context = {
        'statistics_nations': nations,
        'statistics_inventors': inventors_num,
        'statistics_categories': categories,
        'statistics_inventions': inventions_num,
    }

    return render(request, 'statistics.html', context=context)


# def list(request):
#     """
#     View function for home page of site.
#     """
#     # Render the HTML template index.html
#     return render(
#         request,
#         'list.html',
#     )

class InventionListView(ListView):
    model = Invention

    context_object_name = 'inventions_list'   # your own name for the list as a template variable
    template_name = 'invention/list.html'  # Specify your own template name/location
    paginate_by = 6

    def get_queryset(self):
        if 'category_name' in self.kwargs:
            return Invention.objects.filter(category__name=self.kwargs['category_name']).all() # Get 5 books containing the title war
        else:
            return Invention.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_inventions'] = len(self.get_queryset())
        if 'category_name' in self.kwargs:
            context['view_title'] = f"Kategorie: {self.kwargs['category_name']}"
            context['view_head'] = f"Kategorie vynálezu: {self.kwargs['category_name']}"
        else:
            context['view_title'] = 'Vynálezy'
            context['view_head'] = 'Přehled vynálezů'
        return context


class InventionDetailView(DetailView):
    model = Invention

    context_object_name = 'invention_detail'   # your own name for the list as a template variable
    template_name = 'invention/detail.html'  # Specify your own template name/location


class InventionCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Invention

    fields = ['name', 'inventors', 'description', 'date_of_invention', 'category']
    initial = {'date_of_invention': datetime.date.today()}
    template_name = 'inventions/invention_bootstrap_form.html'
    success_url = reverse_lazy('inventions')

    permission_required = "inventions.add_invention"


class InventionUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Invention
    # fields = '__all__'

    template_name = 'inventions/invention_bootstrap_form.html'
    form_class = InventionModelForm

    permission_required = "inventions.change_invention"


class InventionDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Invention

    context_object_name = 'vynalez'
    template_name = 'inventions/invention_confirm_delete.html'
    success_url = reverse_lazy('inventions')

    permission_required = "inventions.delete_invention"
