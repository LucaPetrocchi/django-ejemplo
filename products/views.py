from django.shortcuts import render, redirect

from products.repositories.product import ProductRepository

repo = ProductRepository()

def product_list(request):
    products = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products = products
        )
    )
    
def product_create(request):
    ...
    
def product_detail(request, id):
    product = repo.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {
            'product': product
        }
    )

def product_delete(request, id):
    product = repo.get_by_id(id)
    repo.delete(product)
    return redirect('product_list')
    
def product_update(request, id):
    ...
    
