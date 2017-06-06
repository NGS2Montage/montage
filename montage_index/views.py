from django.shortcuts import render

def index(request):
    return render(request, 'montage_index/index.html')

def viewer(request, match):
    return render(request, 'montage_index/viewer.html')

def project(request, match=None):
    return render(request, 'montage_index/project.html')
