from django.shortcuts import render
from phoneBook.models import Category, Phone
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from phoneBook.forms import PhoneForm, CategoryForm
from django.urls import reverse_lazy
# Create your views here.


class IndexView(ListView):
    model = Phone
    template_name = "phoneBook/index.html"
    context_object_name = "phones"
    queryset = Phone.objects.filter(activate=1, isHome=1)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class PhoneDetailView(DetailView):
    model = Phone
    template_name = "phoneBook/phone-detail.html"
    context_object_name = "phone"
    
    
class CategoryPhoneListView(ListView):
    template_name = "phoneBook/list.html"
    context_object_name = "phones"
    paginate_by = 2
    
    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Phone.objects.filter(kategori__slug=slug, activate=1)
    
    def get_context_Data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["seciliKategori"] = self.kwargs["slug"]
        return context
    
    
class PhoneCreateView(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = "phoneBook/phone-create.html"
    success_url = reverse_lazy("index")
    
class PhoneListView(ListView):
    model = Phone
    template_name = "phoneBook/phone-list.html"
    context_object_name = "phones"
    
class PhoneEditView(UpdateView):
    model = Phone
    template_name = "phoneBook/phone-edit.html"
    form_class = PhoneForm
    context_object_name = "phone"
    success_url = reverse_lazy("phone-list")
    
class PhoneDeleteView(DeleteView):
    model = Phone
    template_name = "phoneBook/phone-delete.html"
    context_object_name = "phone"
    success_url = reverse_lazy("phone-list")
    
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "phoneBook/category-create.html"
    success_url = reverse_lazy("index")