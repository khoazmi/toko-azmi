import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_product = models.CharField(max_length=50, default='Masukan Nama Produk')
    price = models.IntegerField(default='0')
    description = models.TextField(max_length=400, default='Tambahkan Deskripsi (max: 400 kata)')
