from django.urls import path, include
from . import views

urlpatterns = [

    path('Error/', views.Error, name='error'),
    path('logout', views.logout, name='logout'),

    path('index/', views.Adminindex, name='adminhome'),
    path('Districtreg/', views.Districtreg, name='Districtreg'),
    path('Districtview/', views.Districtview, name='Districtview'),
    path('Districtedit/<int:id>/', views.Districtedit, name='Districtedit'),
    path('Districtdelete/<int:id>/', views.Districtdelete, name='Districtdelete'),

    path('Locationreg/', views.Location, name='Location'),
    path('Locationview/', views.Locationview, name='Locationview'),
    path('Locations/', views.locationbyid, name='locationbyid'),
    path('Locationedit/<int:id>/', views.Locationedit, name='Locationedit'),
    path('Locationdelete/<int:id>/', views.Locationdelete, name='Locationdelete'),

    path('Categoryreg/', views.Categoryreg, name='Categoryreg'),
    path('Categoryview/', views.Categoryview, name='Categoryview'),
    path('Categoryedit/<int:id>/', views.Categoryedit, name='Categoryedit'),
    path('Categorydelete/<int:id>/', views.categorydelete, name='Categorydelete'),
    path('subcatbycat/', views.subcatbycat, name='subcatbycat'),

    path('Subcategoryreg/', views.subcatreg, name='subcategory'),
    path('Subcategoryview/', views.subcateview, name='subcategoryview'),
    path('Subcategorydelete/<int:id>', views.subcatedelete, name='subcategorydelete'),

    path('SellerRequests/', views.Requestsbysellers, name='Sellerreq'),
    path('ViewAcceptedSeller/', views.ViewAcceptedSeller, name='ViewAcceptedSeller'),
    path('SellerAccept/<int:id>/', views.verify, name='SellerAccept'),
    path('SellerReject/<int:id>/', views.Reject, name='SellerReject'),

]
