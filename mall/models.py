from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/mall/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    since = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    info_text = MarkdownxField()
    img = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    price = models.CharField(max_length=10)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    calories = models.CharField(max_length=10)
    gram = models.CharField(max_length=10)
    nutrition_img = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.name} ({self.price}원)'

    def get_absolute_url(self):
        return f'/mall/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.info_text)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()

        else:
            return 'https://doitdjango.com/avatar/id/475/21399d185a8ff82e/svg/{self.author.email}/'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()

        else:
            return 'https://doitdjango.com/avatar/id/475/21399d185a8ff82e/svg/{self.author.email}/'
