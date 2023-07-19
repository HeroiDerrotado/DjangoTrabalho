from django.shortcuts import render

# Create your views here.

def especies_views(request):
    return render(request,"especies/paginas/especies_body.html")
