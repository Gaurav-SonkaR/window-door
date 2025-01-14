from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"index.html")

def products_page(request):
    return render(request,"products.html")