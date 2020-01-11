from django.db import models

# Create your models here.
class PostModels(models.Model):
    judul = models.CharField(max_length=50)
    body = models.TextField()
    penulis = models.CharField(max_length=50)

    LIST_KATEGORI = (
        ('Berita', 'berita'),
        ('Info', 'info'),
        ('Jurnal', 'jurnal'),
    )

    kategori = models.CharField(
        max_length=50,
        choices=LIST_KATEGORI,
        default='BRT'
        )

    timeUpdate = models.DateField(auto_now=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.id}. {self.judul}"
    