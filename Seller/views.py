from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_control
from ADMIN.models import Tbl_District, Tbl_Location, Tbl_Category, Tbl_Subcategory
from Guest.models import Login
from Seller.models import Tbl_Product


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    logid = request.session.get('Loginid')
    logname = request.session.get('Uname')
    if logid:
        return render(request, "Seller/index.html", {'Loginid': logid, 'Logname': logname})
    else:
        return HttpResponse(
            "<script>alert('Authentication Required  Please login first');window.location='/login';</script>")


def logout(request):
    if "Loginid" in request.session:
        del request.session["Loginid"]
        del request.session['Uname']
        return redirect('/')


def productreg(request):
    if request.method == 'POST':
        subcategory = request.POST.get("subcategory")
        productname = request.POST.get("productname")
        productprice = request.POST.get("productprice")
        productstock = request.POST.get("productstock")
        productdesc = request.POST.get("productdesc")

        prdobj = Tbl_Product()
        if Tbl_Product.objects.filter(Productname=productname).exists():
            return HttpResponse(
                "<script>alert('Product Already Exist');window.location='/Seller/productreg';</script>")
        prdobj.Subcategoryid = Tbl_Subcategory.objects.get(Subcategoryid=subcategory)
        prdobj.Productname = productname
        prdobj.Productdesc = productdesc
        prdobj.Productprice = productprice
        prdobj.ProductStock = productstock
        prdobj.Sellerid = Login.objects.get(Loginid=request.session['Loginid'])

        if len(request.FILES) != 0:
            image1 = request.FILES['prdimg1']
        else:
            image1 = 'default.jpg'
        prdobj.productimage1 = image1
        if len(request.FILES) != 0:
            image2 = request.FILES['prdimg2']
        else:
            image2 = 'default.jpg'
        prdobj.productimage2 = image2
        prdobj.save()
        return HttpResponse(
            "<script>alert('Product Sucessfully Added');window.location='/Seller/viewproduct';</script>")
    cat = Tbl_Category.objects.all()
    return render(request, "Seller/productreg.html", {'Category': cat})


def categorybyid(request):
    categoryid = int(request.POST.get('cat'))
    catbyid = Tbl_Subcategory.objects.filter(Categoryid=categoryid).values()
    return JsonResponse(list(catbyid), safe=False)


def viewproduct(request):
    loginid = request.session['Loginid']
    cat = Tbl_Category.objects.all()
    # cat = Tbl_Product.objects.filter(Sellerid_id=loginid).select_related('Subcategoryid__Categoryid').values('Subcategoryid__Categoryid__Categoryname').distinct()
    pro = Tbl_Product.objects.filter(Sellerid=loginid)
    return render(request, "Seller/productview.html", {'Category': cat, 'products': pro})


def productbysubcatid(request):
    login = request.session.get('Loginid')
    Subcategory = int(request.POST.get('subcat'))
    productid = Tbl_Product.objects.filter(Subcategoryid=Subcategory, Sellerid=login).values()
    return JsonResponse(list(productid), safe=False)


def productedit(request, id):
    if request.method == 'POST':
        prd = Tbl_Product.objects.get(Productid=id)
        prd.Productname = request.POST.get("productname")
        prd.Productdesc = request.POST.get("productdesc")
        prd.Productprice = request.POST.get("productprice")
        prd.ProductStock = request.POST.get("productstock")
        if len(request.FILES) == 0:
            prd.productimage1 = request.POST.get("prdimg1old")
        else:
            prd.productimage1 = request.FILES["prdimg1"]

        if len(request.FILES) == 0:
            prd.productimage2 = request.POST.get("prdimg2old")
        else:
            prd.productimage2 = request.FILES["prdimg2"]

        prd.Subcategoryid = Tbl_Subcategory.objects.get(Subcategoryid=request.POST.get("subcategory"))
        return HttpResponse(
            "<script>alert('Product Updated Sucessfully');window.location='/Seller/viewproduct';</script>")
    else:
        product = Tbl_Product.objects.get(Productid=id)
        cat = Tbl_Category.objects.all()
        return render(request, "Seller/productedit.html", {'Category': cat, 'pro': product})


def productdelete(request, id):
    product = Tbl_Product.objects.get(Productid=id)
    product.delete()
    return viewproduct(request)
