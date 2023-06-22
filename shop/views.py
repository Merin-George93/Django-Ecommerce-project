from django.shortcuts import render
from shop.models import Product,Category
from django.contrib.auth.models import User # reg
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'category.html')

def category(request):
    p=Category.objects.all()
    return render(request,'category.html',{'c': p})


def products(request,cslug):
    p=Product.objects.filter(category__slug=cslug)
    return render(request,'product.html',{'c': p})


def prodetail(request, pslug):
    p = Product.objects.get(slug=pslug)
    return render(request, 'detail.html', {'p': p})


def register(request):
    if(request.method=='POST'): # condition
        f=request.POST['f']
        l=request.POST['l']
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        if p==cp: # confirm entered credentials
            user = User.objects.create_user(first_name=f,last_name=l,username=u,password=p,)# model creation
            user.save() # saving created model
            return home(request)
    return render(request,'signup.html',)

def usersignin(request):
    if(request.method=='POST'):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,'Invalid credentials')

    return render(request,'login.html')

def usersignout(request):
    logout(request)
    return home(request)


