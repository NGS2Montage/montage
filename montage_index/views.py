from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'montage_index/index.html')

def viewer(request, match):
    return render(request, 'montage_index/viewer.html')

def project(request, match=None):
    return render(request, 'montage_index/project.html')

def data(request, match=None):
    return render(request, 'montage_index/data.html')

def content(request, name=None):
    logger.debug("Loading" + name)
    return render(request, 'montage_index/content/' + name + '.html')
