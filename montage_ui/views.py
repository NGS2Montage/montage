from django.shortcuts import render
from django.conf import settings
import logging

if settings.DEBUG:
    logger = logging.getLogger(__name__)

def index(request):
    if settings.DEBUG:
        logger.debug(request)
    return render(request, 'montage_ui/index.html')

def viewer(request, match):
    return render(request, 'montage_ui/viewer.html')

def project(request, match=None):
    return render(request, 'montage_ui/project.html')

def data(request, match=None):
    return render(request, 'montage_ui/data.html')

def content(request, name=None):
    if settings.DEBUG:
        logger.debug(request)
    return render(request, 'montage_ui/content/' + name + '.html')

def page(request, name=None):
    if settings.DEBUG:
        logger.debug(request)
    return render(request, 'montage_ui/page.html',{'name':name})
