from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from ADMIN.models import Tbl_Subcategory, Tbl_Category
from Customer.models import Tbl_cart
from Seller.models import Tbl_Product


# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    logid = request.session.get('Loginid')
    logname = request.session.get('Uname')
    if logid:
        category = Tbl_Category.objects.all()
        subcategory = Tbl_Subcategory.objects.all()
        products = Tbl_Product.objects.all()
        prices = [product.Productprice for product in products]

        # Add 100 to each price and store the results in a new list
        amounts = [price + 100 for price in prices]
        # return HttpResponse(amounts)

        return render(request, "Customer/index.html",
                      {'Loginid': logid, 'Logname': logname, 'category': category, 'subcategory': subcategory,
                       'product': products, 'amounts': amounts})
    else:
        return HttpResponse(
            "<script>alert('Authentication Required  Please login first');window.location='/login';</script>")


def logout(request):
    if "Loginid" in request.session:
        del request.session["Loginid"]
        del request.session['Uname']
        return redirect('/login/')


def handler404(request, exception):
    return render(request, 'error.html', {'error_message': 'Page not found'}, status=404)


def viewmore(request, id):
    prd = Tbl_Product.objects.get(Productid=id)
    return render(request, "Customer/productviewmore.html", {'product': prd})


def category(request):
    cat = Tbl_Category.objects.all()
    subcatcount = Tbl_Category.objects.annotate(product_count=Count('tbl_subcategory'))
    return render(request, "Customer/Category.html", {'category': cat, 'subcategorycount': subcatcount})


def subcategory(request, id):
    subcat = Tbl_Subcategory.objects.filter(Categoryid=id)
    cat = Tbl_Category.objects.get(Categoryid=id)
    return render(request, "Customer/subcategory.html", {'subcategory': subcat, 'cat': cat})


def products(request, id):
    prod = Tbl_Product.objects.filter(Productid=id)
    return render(request, "Customer/Products.html", {'product': prod})


def cart(request, id):
    if request.method == 'POST':
        cart = Tbl_cart()
        cart.Productid = request.POST.get("name")
        cart.Productid = request.POST.get("name")
        cart.loginid = request.POST.get("name")
        cart.Quantity = request.POST.get("name")
        cart.Status = 'Carted'

    # prod = Tbl_Product.objects.filter(Productid=id)
    return render(request, "Customer/Cart.html")


def cartview(request):
    login = request.session.get('Loginid')
    # prod = Tbl_Product.objects.filter(Productid=id)
    return render(request, "Customer/Cart.html")
