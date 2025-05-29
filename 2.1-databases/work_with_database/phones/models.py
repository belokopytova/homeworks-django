from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=300)
    release_date = models.CharField(max_length=15)
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50)



