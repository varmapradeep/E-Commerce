from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from ADMIN.models import Tbl_District, Tbl_Location
from Guest.models import Login, Tbl_Customer, Tbl_Seller


def index(request):
    return render(request, "Guest/index.html")


def login(request):
    if request.method == 'POST':
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        if Login.objects.filter(Username=Username, Password=Password).exists():
            Logindata = Login.objects.get(Username=Username, Password=Password)
            request.session['Uname'] = Logindata.Username
            request.session['Loginid'] = Logindata.Loginid
            role = Logindata.Role
            status = Logindata.Status
            if role == "Admin":
                return redirect('/Admin/index')
                # return render(request, "Admin/index.html")
            elif role == "Seller" and status == "Accepted":
                return redirect('/Seller/index')
                # return render(request, "Customer/index.html")
            elif role == "Customer" and status == "Accepted":
                return redirect('/Customer/index')
            else:
                return HttpResponse("NOT Approved")
        else:
            context = {"error": "Incorrect Username or Password"}
            return render(request, "Guest/Login.html", context)
    else:
        # return HttpResponse("haii")
        return render(request, "Guest/Login.html")


def locationbyid(request):
    Districtbyid = int(request.POST.get('did'))
    locationbyid = Tbl_Location.objects.filter(Districtid=Districtbyid).values()
    return JsonResponse(list(locationbyid), safe=False)


def Customerreg(request):
    if request.method == 'POST':
        custobj = Tbl_Customer()
        loginobj = Login()
        custobj.Customername = request.POST.get("name")
        custobj.email = request.POST.get("email")
        if Tbl_Customer.objects.filter(email=request.POST.get("email")).exists():
            return HttpResponse(
                "<script>alert('E-mail Already Exist');window.location='../Customerreg';</script>")
        custobj.Gender = request.POST.get("gender")
        custobj.Phone = request.POST.get("phone")
        custobj.locationid = Tbl_Location.objects.get(Locationid=request.POST.get("location"))
        custobj.Housename = request.POST.get("housename")
        custobj.pincode = request.POST.get("pincode")
        loginobj.Username = request.POST.get("username")
        if Login.objects.filter(Username=request.POST.get("username")).exists():
            return HttpResponse(
                "<script>alert('Username Already Exist');window.location='../Customerreg';</script>")
        loginobj.Password = request.POST.get("password")
        loginobj.Role = 'Customer'
        loginobj.Status = 'Accepted'
        if len(request.FILES) != 0:
            catimg = request.FILES['image']
        else:
            catimg = 'Images/default.jpg'
        custobj.Customerimage = catimg
        custobj.Loginid = loginobj
        loginobj.save()
        custobj.save()
        return HttpResponse(
            "<script>alert('Customer Registered Sucessfully');window.location='../login';</script>")

    else:
        dist = Tbl_District.objects.all()
        return render(request, "Guest/Customerreg.html", {'district': dist})


def Sellerreg(request):
    if request.method == 'POST':
        sellerobj = Tbl_Seller()
        loginobj = Login()
        sellerobj.Sellername = request.POST.get("name")
        sellerobj.Selleremail = request.POST.get("email")
        if Tbl_Seller.objects.filter(Selleremail=request.POST.get("email")).exists():
            return HttpResponse(
                "<script>alert('E-mail Already Exist');window.location='../Sellerreg';</script>")
        sellerobj.SellerGender = request.POST.get("gender")
        sellerobj.SellerPhone = request.POST.get("phone")
        sellerobj.locationid = Tbl_Location.objects.get(Locationid=request.POST.get("location"))
        sellerobj.Housename = request.POST.get("housename")
        sellerobj.pincode = request.POST.get("pincode")
        loginobj.Username = request.POST.get("username")
        if Login.objects.filter(Username=request.POST.get("username")).exists():
            return HttpResponse(
                "<script>alert('Username Already Exist');window.location='../Sellerreg';</script>")
        loginobj.Password = request.POST.get("password")
        loginobj.Role = 'Seller'
        loginobj.Status = 'Requested'
        if len(request.FILES) != 0:
            idproof = request.FILES['idproof']
        else:
            idproof = 'Images/default.jpg'
        sellerobj.Idproof = idproof

        if len(request.FILES) != 0:
            catimg = request.FILES['image']
        else:
            catimg = 'Images/default.jpg'
        sellerobj.Sellerimage = catimg
        sellerobj.Loginid = loginobj
        loginobj.save()
        sellerobj.save()
        return HttpResponse(
            "<script>alert('Seller Registered Sucessfully Plese Wait untill Admin Approve Your Request');window.location='../login';</script>")

    else:
        dist = Tbl_District.objects.all()
        return render(request, "Guest/Sellerreg.html", {'district': dist})
