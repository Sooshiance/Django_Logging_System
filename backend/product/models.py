from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
