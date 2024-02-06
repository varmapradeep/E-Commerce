from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login, name="login"),
    path('Customerreg/', views.Customerreg, name='custreg'),
    path('Sellerreg/', views.Sellerreg, name='Sellerreg')

]
