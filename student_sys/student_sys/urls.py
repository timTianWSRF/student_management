"""student_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from student.views import index
from student.views import test,test2,upload_file
from django.views.static import serve
from . import settings


app_name = 'student'
urlpatterns = [
    url(r'test/', test, name='test'),
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^staticfiles/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'test2/', test2),
    url(r'^uploadFile/$', upload_file)
]

