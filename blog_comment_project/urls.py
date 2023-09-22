"""blog_comment_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.blog_detail, name='blog_detail'),
    path('new/', views.create_blog, name='create_blog'),
    path('edit/<int:post_id>', views.edit_blog, name='edit_blog'),
    path('delete/<int:post_id>', views.delete_blog, name='delete_blog'),
    path('comment/<int:post_id>', views.add_comment, name='add_comment'),
    path('delete/<int:post_id>', views.delete_comment, name='delete_comment'),
]
