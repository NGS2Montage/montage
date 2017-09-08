"""django_montage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from montage_ui import views  as ui
from rafter_user_service.urls import router

urlpatterns = [
    url(r'^$', ui.index),
    url(r'^viewer', ui.viewer),
    url(r'^project', ui.project),
    url(r'^data', ui.data),
    url(r'^content/(?P<name>.*)$', ui.content),
    url(r'^page/(?P<name>.*)$', ui.page),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('registration.backends.admin_approval.urls')),
    url(r'^api/', include(router.urls, namespace='api')),
]
