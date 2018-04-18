from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {}
    index_homepage = render(request,"myblog2.0.html",context)
    return index_homepage
