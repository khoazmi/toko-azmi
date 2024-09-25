import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=50, default='Masukan Nama Produk')
    price = models.IntegerField(default='0')
    description = models.TextField(max_length=400, default='Tambahkan Deskripsi (max: 400 kata)')
