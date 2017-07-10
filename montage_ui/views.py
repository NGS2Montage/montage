from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.debug(request)
    return render(request, 'montage_ui/index.html')

def viewer(request, match):
    return render(request, 'montage_ui/viewer.html')

def project(request, match=None):
    return render(request, 'montage_ui/project.html')

def data(request, match=None):
    return render(request, 'montage_ui/data.html')

def content(request, name=None):
    logger.debug("Loading" + name)
    return render(request, 'montage_ui/content/' + name + '.html')
