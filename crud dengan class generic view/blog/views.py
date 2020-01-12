from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView,UpdateView,DeleteView,CreateView
from .models import ArtikelModel
from django.db.models import Q
from .forms import ArtikelForm
from django.urls import reverse_lazy

class ArtikelDelete(DeleteView):
    model = ArtikelModel
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/artikel_delete.html'


class ArtikelUpdate(UpdateView):
    model = ArtikelModel
    form_class = ArtikelForm
    template_name = 'blog/artikelmodel_form.html'
    success_url = reverse_lazy('blog:index')


class ArtikelCreate(CreateView):
    model = ArtikelModel
    fields = ['judul','isi','penulis']
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'Create Article'
        return context

# class ArtikelFormView(FormView):
#     form_class = ArtikelForm
#     template_name = 'blog/create.html'
#     success_url = reverse_lazy('blog:index')

#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page_title"] = 'Create Article'
#         return context
    

class ArtikelList(ListView):
    model = ArtikelModel
    template_name = 'blog/artikel_list.html'
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title1"] = 'Blog'
        context["page_title2"] = 'Article List'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            cari = ArtikelModel.objects.filter(
                Q(judul__icontains=query) | Q(penulis__icontains=query)
            )
        else:
            cari = ArtikelModel.objects.all()

        return cari
    
class ArtikelDetail(DetailView):
    model = ArtikelModel
    template_name = 'blog/artikel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title1"] = 'Blog'
        context["page_title2"] = 'Detail Article'
        return context
        
    

