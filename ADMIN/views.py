from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_control
from ADMIN.models import Tbl_District, Tbl_Location, Tbl_Category, Tbl_Subcategory
from Guest.models import Tbl_Seller, Login


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Adminindex(request):
    logid = request.session.get('Loginid')
    logname = request.session.get('Uname')
    if logid:
        return render(request, "Admin/index.html", {'Loginid': logid, 'Logname': logname})
    else:
        return HttpResponse(
            "<script>alert('Authentication Required  Please login first');window.location='/login';</script>")


def Error(request):
    return render(request, "Admin/error.html")


def logout(request):
    if "Loginid" in request.session:
        del request.session["Loginid"]
        del request.session['Uname']
        return redirect('/')


def Districtreg(request):
    # return render(request, "Admin/districtreg.html")
    if request.method == 'POST':
        Districtname = request.POST.get("District")
        district = Tbl_District()

        if Tbl_District.objects.filter(Districtname=Districtname).exists():
            # context = {"error": "Invalid District Name"}
            # return render(request, "Admin/districtreg.html", context)
            return HttpResponse(
                "<script>alert('District Name Already Exist');window.location='/Admin/Districtview';</script>")
        district.Districtname = Districtname
        district.save()
        return HttpResponse(
            "<script>alert('District Inserted');window.location='/Admin/Districtview';</script>")
    else:
        return render(request, "Admin/districtreg.html")


def Districtview(request):
    dist = Tbl_District.objects.all()
    return render(request, "Admin/districtview.html", {'district': dist})


def Districtedit(request, id):
    if request.method == 'POST':
        Districtname = request.POST.get("District")
        dist = Tbl_District.objects.get(Districtid=id)
        dist.Districtname = Districtname
        dist.save()
        return Districtview(request)
    dist = Tbl_District.objects.get(Districtid=id)
    return render(request, "Admin/districtedit.html", {'dist': dist})


def Districtdelete(request, id):
    dist = Tbl_District.objects.get(Districtid=id)
    dist.delete()
    return Districtview(request)


def Location(request):
    # return render(request, "Admin/districtreg.html")
    if request.method == 'POST':
        Districtid = request.POST.get("Districtid")
        Location = request.POST.get("Location")
        locobj = Tbl_Location()
        if Tbl_Location.objects.filter(Districtid=Districtid, Locationname=Location).exists():
            return HttpResponse(
                "<script>alert('Location Name Already Exist');window.location='/Admin/Locationreg';</script>")
        locobj.Districtid = Tbl_District.objects.get(Districtid=Districtid)
        locobj.Locationname = Location
        locobj.save()
        return HttpResponse(
            "<script>alert('Location Inserted');window.location='/Admin/Locationview';</script>")
    else:
        dist = Tbl_District.objects.all()
        return render(request, "Admin/locationreg.html", {'district': dist})


def Locationview(request):
    loc = Tbl_Location.objects.all()
    dist = Tbl_District.objects.all()
    return render(request, "Admin/locationview.html", {'location': loc, 'district': dist})


def locationbyid(request):
    Districtbyid = int(request.POST.get('did'))
    locationbyid = Tbl_Location.objects.filter(Districtid=Districtbyid).values()
    return JsonResponse(list(locationbyid), safe=False)


def Categoryreg(request):
    if request.method == 'POST':
        catname = request.POST.get("Category")
        catdesc = request.POST.get("Categorydesc")
        catobj = Tbl_Category()
        catobj.Categoryname = catname
        catobj.Categorydesc = catdesc
        if len(request.FILES) != 0:
            catimg = request.FILES['Categoryimage']
        else:
            catimg = 'Images/default.jpg'
        catobj.Categoryimg = catimg
        catobj.save()
        return HttpResponse(
            "<script>alert('Category Registered Sucessfully');window.location='/Admin/Categoryview';</script>")
    else:
        return render(request, "Admin/Categoryreg.html")


def Categoryview(request):
    cate = Tbl_Category.objects.all()
    return render(request, "Admin/categoryview.html", {'category': cate})


def Locationdelete(request, id):
    loc = Tbl_Location.objects.get(Locationid=id)
    loc.delete()
    return Locationview(request)


def Categoryedit(request, id):
    if request.method == 'POST':
        cate = Tbl_Category.objects.get(Categoryid=id)
        cate.Categoryname = request.POST.get('Category')
        cate.Categorydesc = request.POST.get('Categorydesc')
        if len(request.FILES) == 0:
            cate.Categoryimg = request.POST.get("Catimage")
        else:
            cate.Categoryimg = request.FILES["Categoryimage"]
        cate.save()
        return Categoryview(request)
    else:
        category = Tbl_Category.objects.get(Categoryid=id)
        return render(request, "Admin/Categoryedit.html", {'cat': category})


def categorydelete(request, id):
    cate = Tbl_Category.objects.get(Categoryid=id)
    cate.delete()
    return Categoryview(request)


def Locationedit(request, id):
    if request.method == 'POST':
        Districtid = request.POST.get("Districtid")
        Location = request.POST.get("Location")
        loc = Tbl_Location.objects.get(Locationid=id)
        loc.Locationname = Location
        loc.Districtid = Tbl_District.objects.get(Districtid=Districtid)
        loc.save()
        return Locationview(request)
    else:
        loct = Tbl_Location.objects.get(Locationid=id)
        dist = Tbl_District.objects.all()
        return render(request, "Admin/locationedit.html", {'loc': loct, 'dist': dist})


def subcatreg(request):
    if request.method == 'POST':
        Categoryid = request.POST.get("categortid")
        Subcategoryname = request.POST.get("subcategory")
        Subcategorydesc = request.POST.get("subcategorydec")
        Subcategoryimg = request.POST.get("subcategoryimg")

        subcatobj = Tbl_Subcategory()
        if Tbl_Subcategory.objects.filter(Subcategoryname=Subcategoryname).exists():
            return HttpResponse(
                "<script>alert('Subcategory Already Exist');window.location='/Admin/Subcategoryreg';</script>")
        subcatobj.Categoryid = Tbl_Category.objects.get(Categoryid=Categoryid)
        subcatobj.Subcategoryname = Subcategoryname
        subcatobj.Subcategorydesc = Subcategorydesc
        if len(request.FILES) != 0:
            subcatimg = request.FILES['subcategoryimg']
        else:
            subcatimg = 'default.jpg'
        subcatobj.Subcategoryimg = subcatimg
        subcatobj.save()
        return HttpResponse(
            "<script>alert('Subcategory Inserted');window.location='/Admin/Subcategoryview';</script>")
    else:
        cat = Tbl_Category.objects.all()
        return render(request, "Admin/Subcategoryreg.html", {'categ': cat})


def subcateview(request):
    subcat = Tbl_Subcategory.objects.all()
    cat = Tbl_Category.objects.all()
    return render(request, "Admin/Subcategoryview.html", {'subcategory': subcat, 'category': cat})


def subcatedelete(request, id):
    subcat = Tbl_Subcategory.objects.get(Subcategoryid=id)
    subcat.delete()
    return subcateview(request)


def subcatbycat(request):
    category = int(request.POST.get('cat'))
    subcategory = Tbl_Subcategory.objects.filter(Categoryid=category).values()
    return JsonResponse(list(subcategory), safe=False)


def Requestsbysellers(request):
    Seller = Tbl_Seller.objects.filter(Loginid__Status="Requested", Loginid__Role='Seller')
    return render(request, "Admin/Sellerrequest.html", {'sellerrequest': Seller})


def ViewAcceptedSeller(request):
    Seller = Tbl_Seller.objects.filter(Loginid__Status="Accepted", Loginid__Role='Seller')
    return render(request, "Admin/ViewSellers.html", {'sellerrequest': Seller})


def verify(request, id):
    login = Login.objects.get(Loginid=id)
    login.Status = "Accepted"
    login.save()
    return Requestsbysellers(request)


def Reject(request, id):
    login = Login.objects.get(Loginid=id)
    login.Status = "Rejected"
    login.save()
    return Requestsbysellers(request)
