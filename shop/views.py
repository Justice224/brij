from __future__ import unicode_literals
from django.shortcuts import render,reverse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shop.models import *
from shop.forms import *
from registration.backends.simple.views import RegistrationView



class RangoRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')


def index(request):
    categories = Category.objects.all()
    hot = Product.objects.filter(hot="yes")[:4]
    context = {
       'categories': categories,
        'hot': hot
    }
    return render(request, 'shop/index.html', context)


def login(request):
    return render(request, 'shop/login.html', {})


def register(request):
    registered = False
#    print request.user
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            pass  
            #print user_form.errors,profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered,
    }
    return render(request,'shop/register.html',context)

def about(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'shop/about.html', context)


def category(request,category_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'category':category,
        'categories':categories
    }
    return render(request, 'shop/category.html',context)


def checkout(request):
    return render(request, 'shop/checkout.html', {})


def search(request):
    categories = Category.objects.all()
    if request.method =='POST':
        product = request.POST.get('Product','')


        try:
            product = Product.objects.filter(name__icontains=product)
        except Product.DoesNotExist:
            pass

        context = {
            'product':product,
            'categories': categories
        }
        return render(request,'shop/single.html',context)

