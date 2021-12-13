from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/mall/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=30)
    info_text = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    price = models.CharField(max_length=10)
    # brand = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    calories = models.CharField(max_length=10)
    gram = models.CharField(max_length=10)
    nutrition_img = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.name} ({self.price}원)'

    def get_absolute_url(self):
        return f'/mall/{self.pk}/'


