from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('success/', views.success, name='success'),
    path('review/', views.add_review, name='add_review'),
    path('admin-reviews/', views.admin_reviews, name='admin_reviews'),
    path('admin-queries/', views.admin_queries, name='admin_queries'),
]


