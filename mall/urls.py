from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('category/<str:slug>', views.category_page),
    path('create_product/', views.ProductCreate.as_view()),
    path('update_product/<int:pk>/', views.ProductUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('search/<str:q>/', views.ProductSearch.as_view()),
    path('cart/<int:pk>', views.cart, name="cart"),
]