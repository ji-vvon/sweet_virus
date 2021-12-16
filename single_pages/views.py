from django.shortcuts import render
from mall.models import Product, Comment

def landing(request):
    recent_products = Product.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html', {'recent_products': recent_products})

def about_us(request):
    return render(request, 'single_pages/about_us.html')

def mypage(request):
    if request.user.is_authenticated:
        me = request.user
        comments = Comment.objects.all().filter(author=me).order_by('-id')
        return render(request, 'single_pages/mypage.html', {'comments': comments})
    else:
        return render(request, 'single_pages/mypage.html')
