import datetime

from django.db import models
from django.utils import timezone


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_rate = models.IntegerField(default=0)
    product_pub_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return '{}: {}/Q'.format(self.product_name.upper(), str(self.product_rate))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
