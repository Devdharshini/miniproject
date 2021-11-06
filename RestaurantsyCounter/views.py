from django.shortcuts import render,redirect
from django.http import response
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm
from .models import login
from Restaurantsy.models import Carts,kfc

# Create your views here.

def index(request):
    if request.method == "POSt":
        name = request.POST['username']
        password = request.POST['password']
        check = login.get_counter_by_name(name)
        if check is not None:
            return redirect('homepage')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('loginpage')
    else:
        form = LoginForm()
        return render(request, "RestaurantsyCounter/LoginPage.html",{"form":form})
        #try:
        #    authentication = render_to_string("RestaurantsyCounter/LoginPage.html",{"form":form})
        #return HttpResponse(authentication)
        #except:
        #return HttpResponseNotFound("<h1>404 error. Page not found!</h1>")

class homepage(View):
    def get(self,request):
        ids = [e.item for e in Carts.objects.all()]
        product = kfc.get_item_by_id(ids)
        c = Carts.objects.all()
        try:
            home = render_to_string("RestaurantsyCounter/HomePage.html",{"products":product, "cart":c})
            return HttpResponse(home)
        except:
            return HttpResponseNotFound("<h1>404 error. Page not found!</h1>")

class delivered(View):
    def get(self,request):
        ids = [e.item for e in Carts.objects.all()]
        product = kfc.get_item_by_id(ids)
        c = Carts.objects.all()
        try:
            delivered = render_to_string("RestaurantsyCounter/delivered.html",{"products":product, "cart":c})
            return HttpResponse(delivered)
        except:
            return HttpResponseNotFound("<h1>404 error. Page not found!</h1>")   

#class delivered1(View):
#    def get(self,request):
#        ids = [e.item for e in Carts.objects.all()]
#        product = kfc.get_item_by_id(ids)
#        c = Carts.objects.all()
def delivers(request):
    ids = [e.item for e in Carts.objects.all()]
    product = kfc.get_item_by_id(ids)
    c = Carts.objects.all()
    try:
        delivered = render_to_string("RestaurantsyCounter/delivers.html",{"product":product, "cart":c})
        return HttpResponse(delivered)
    except:
        return HttpResponseNotFound("<h1>404 error. Page not found!</h1>")   
