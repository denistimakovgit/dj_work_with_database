from django.db import models
import psycopg2

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to=None)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50)
