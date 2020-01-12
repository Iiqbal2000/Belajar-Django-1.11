from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class ArtikelModel(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField()
    penulis = models.CharField(max_length=50)
    publish = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'slug':self.slug})
    
    def __str__(self):
        return f'{self.id}. {self.judul}'
    
