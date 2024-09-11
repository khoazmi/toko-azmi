from django.db import models

class Product(models.Model):
    nama_siswa = models.CharField(max_length=50)
    kelas_siswa = models.CharField(max_length=50)
    name_product = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=400)
