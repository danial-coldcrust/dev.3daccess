"""
Definition of urls for DjangoWebProject2.
"""

from django.urls import include, re_path
from django.contrib import admin



urlpatterns = [
   
   re_path('^blog$', include('blog.urls',namespace='blog')),
   re_path('^admin/', admin.site.urls),
   
]
