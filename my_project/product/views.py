from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all().order_by('id')
    contex = {
        'page_title' : "Products",
        'another_content' : "This is another content",
        'products' : products
    }
    return render(request,'index.html',contex)


def detail(request,product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f'<h1>This is the page of {product.name}</h1>')

def create(request):
    contex = {
        'page_title' : "Create Product"
    }
    if request.method == "POST":
        post_data = request.POST
        new_product = Product(name=post_data['name'], description=post_data['description'], category=post_data['category'], created_at = '2020-01-01')
        new_product.save()
        return HttpResponseRedirect('/product/list')
    else:
        print("In the get request")
        return render(request,'create.html',contex)