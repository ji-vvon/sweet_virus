from django.shortcuts import render
from mall.models import Product, Comment, Cart, Category


def landing(request):
    recent_products = Product.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html', {'recent_products': recent_products})


def about_us(request):
    categories = Category.objects.all()
    no_category_product_count = Product.objects.filter(category=None).count()
    return render(request, 'single_pages/about_us.html',
                  {'categories' : categories, 'no_category_product_count': no_category_product_count})


def mypage(request):
    if request.user.is_authenticated:
        me = request.user
        comments = Comment.objects.all().filter(author=me).order_by('-id')
        carts = Cart.objects.all().filter(author=me).order_by('-id')
        return render(request, 'single_pages/mypage.html', {'comments': comments, 'carts' : carts})

    else:
        return render(request, 'single_pages/mypage.html')
