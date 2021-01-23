from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us' ),
    path('detail/<int:post_id>', views.post_detail, name='detail' )
]
