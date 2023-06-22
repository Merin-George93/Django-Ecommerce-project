from django.contrib import admin
from django.urls import path
from shop import views

app_name='shop'
urlpatterns = [
    path('',views.category,name='category'),
    path('products/<slug:cslug>',views.products,name='products'),
    path('prodetail/<slug:pslug>',views.prodetail,name='prodetail'),
    path('register', views.register, name='register'),
    path('usersignin', views.usersignin, name='usersignin'),
    path('usersignout', views.usersignout, name='usersignout'),

]