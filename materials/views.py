from django.views.generic import *
from django.urls import reverse_lazy
from .models import Material, Category
from .forms import MaterialForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MaterialListView(ListView):
    model = Material
    template_name = 'materials/list.html'
    context_object_name = 'materials'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        if category_id:
            return Material.objects.filter(category_id=category_id)
        return Material.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materials/detail.html'


class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/form.html'
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/form.html'
    success_url = reverse_lazy('materials:list')


class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material
    template_name = 'materials/delete.html'
    success_url = reverse_lazy('materials:list')

class CategoryListView(ListView):
    model = Category
    template_name = 'materials/categories.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'materials/category_form.html'
    success_url = reverse_lazy('materials:categories')