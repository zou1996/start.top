"""zstartop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
<<<<<<< HEAD
from zhomepage.views import homepage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage,name='homepage'),
=======
from django.conf.urls import url
from zhomepage.views import homepage,blog,yyy,detail,msgboard,detail_comment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name='homepage'),
    path('homepage/blog/', blog, name='blog'),
    path('homepage/yyy/', yyy, name='yyy'),
    url(r'^homepage/blog/detail/(?P<page_num>\d+)$', detail, name='detail'),
    url(r'^homepage/blog/detail/(?P<page_num>\d+)/comment$', detail_comment, name='comment'),
    path('homepage/blog/msgboard', msgboard, name='msgboard'),
>>>>>>> 2.2
]
