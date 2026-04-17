from django import forms
from .models import Material, Category


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'description', 'category', 'material_type', 'file', 'link']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']