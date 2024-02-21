from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='customerindex'),
    # path('Error/', views.index, name='customerindex'),

    path('logout/', views.logout, name='logout'),
    path('Viewmore/<int:id>', views.viewmore, name='viewmore'),
    path('category/', views.category, name='custviewcategory'),
    path('subcategory/<int:id>/', views.subcategory, name='custviewsubcategory'),
    path('products/<int:id>/', views.products, name='products'),
    path('Cart/<int:id>/', views.cart, name='Addtocart'),
    path('Cart/', views.cartview, name='cart'),
    path('calculate_total/', views.calculate_total, name='calculate_total'),

    path('Cartprddelete/<int:id>/', views.Cartprddelete, name='Cartprddelete'),

]
