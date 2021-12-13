from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing), #서버IP/아무것도 없음 (대문페이지)
    path('about_us/', views.about_us), #서버IP/about_us/
]