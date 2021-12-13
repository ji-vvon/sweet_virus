from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    info_text = models.CharField(max_length=100, blank=True)
    # img = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    price = models.CharField(max_length=10)
    # brand = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    calories = models.CharField(max_length=10)
    gram = models.CharField(max_length=10)
    # nutrition_img = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.name} ({self.price}원)'

    def get_absolute_url(self):
        return f'/mall/{self.pk}/'


