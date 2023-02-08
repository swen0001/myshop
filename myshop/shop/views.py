from django.shortcuts import render, get_object_or_404

from myshop.shop.models import Category, Product
from myshop.cart.forms import CartAddProductForm
from myshop.shop.recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category).order_by('-created')
    return render(request,
                  'shop/product/list.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'recommended_products': recommended_products})
