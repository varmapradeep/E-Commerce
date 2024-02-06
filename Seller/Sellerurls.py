from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('productreg/', views.productreg, name='productreg'),
    path('categorybyid/', views.categorybyid, name='categorybyid'),
    path('viewproduct/', views.viewproduct, name='viewproduct'),
    path('productbysubcatid/', views.productbysubcatid, name='productbysubcatid'),
    path('Productedit/<int:id>/', views.productedit, name='Productedit'),
    path('Productdelete/<int:id>/', views.productdelete, name='Productdelete'),

]
