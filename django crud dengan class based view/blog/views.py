from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView, RedirectView, View
from .models import PostModels
from .forms import PostForms


class Pengelompokkan:
    
    def get_list_data(self, get_request):
        if len(get_request) == 0:
            sublist = PostModels.objects.all()
        elif get_request.__contains__('content_filter'):
            sublist = PostModels.objects.filter(kategori=get_request['content_filter'])
        else:
            sublist = PostModels.objects.none()
        
        return sublist


class ArticleIndexView(Pengelompokkan,TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, *args, **kwargs):
        kategori_article = self.get_list_data(self.request.GET)
        list_kategori = PostModels.objects.values_list('kategori', flat=True).distinct()
        context = {
            'title':'Blog',
            'content':kategori_article,
            'list_content':list_kategori,
        }            
        return context

class ArticleCreateView(View):
    template_name = "blog/create.html"
    form = PostForms()
    context = {}
    mode = None

    def get(self, *args, **kwargs):
        if self.mode == 'update':
            update_article = PostModels.objects.get(id=kwargs['update_id'])
            data = update_article.__dict__
            self.form = PostForms(initial=data, instance=update_article)

        self.context = {
            'title':'Membuat Artikel',
            'content':self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('update_id'):
            update_article = PostModels.objects.get(id=kwargs['update_id'])
            self.form = PostForms(self.request.POST, instance=update_article)
        else:
            self.form = PostForms(self.request.POST)

        if self.form.is_valid():
            self.form.save()
        
        return redirect('blog:index')


class ArticleDeleteView(RedirectView):
    pattern_name = 'blog:index'

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['delete_id']
        PostModels.objects.filter(id=delete_id).delete()
        return super().get_redirect_url()




