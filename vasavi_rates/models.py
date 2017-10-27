from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_rate = models.IntegerField(default=0)
    bag_weight = models.IntegerField(default=0)
    product_pub_date = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return '{}: {}/Q'.format(self.product_name.upper(), str(self.product_rate))
