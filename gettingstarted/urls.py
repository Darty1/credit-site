from django.urls import path, include, re_path

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('admin/', admin.site.urls),
    path('', hello.views.index, name='index'),
    re_path(r'^login/$', hello.views.LoginView.as_view(), name='login'),
    re_path(r'^register/$', hello.views.RegisterView.as_view(), name='register'),
    re_path(r'logout/$', hello.views.logout, name='logout'),
    re_path(r'^create/$', hello.views.CreateView.as_view(), name='create'),
    re_path(r'^seacrh/$', hello.views.SeacrhView.as_view(), name='search'),
]
