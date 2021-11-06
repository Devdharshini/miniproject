from django.db.models.query import QuerySet
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from .models import kfc,Users,Carts
from django.contrib import messages
from django.views import View
from .forms import SigninForm,LoginForm 

# Create your views here.

def index(request):
    if request.method == 'POST':
        mail = request.POST['Email']
        password = request.POST['Password']
        customer = Users.get_customer_by_mail(mail)
        if customer is not None:
            return redirect('home-page')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login-page')
    else:
        form = LoginForm() 
        return render(request,"Restaurantsy/loginpage.html",{"form":form})


class homepage(View):
    def post(self, request):
        Item = request.POST['id']
        cart = request.POST['quantity']
        if cart is not None:
            items = Carts(
                item  = Item,
                quantity = cart 
            )
            items.save()
            return redirect('home-page')
        else:
            messages.info('add quantity')
            return redirect('home-page')
    def get(self,request):
        items = kfc.objects.all()
        try:
            return render(request,"Restaurantsy/homepage.html",{"items":items})
        except:
            return HttpResponseNotFound("<h1>404 error. Page not found!</h1>")
 
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            detail = Users(
                username = form.cleaned_data['username'],
                phone_no = form.cleaned_data['Phone_no'],
                email = form.cleaned_data['Email'],
                password = form.cleaned_data['Password']
            )
            detail.save()
            return render(request, "Restaurantsy/homepage.html")
    else:
        form = SigninForm()
    return render(request,"Restaurantsy/signin.html",{"form":form})

class CART(View):
    def get(self, request):
        ids = [e.item for e in Carts.objects.all()]
        product = kfc.get_item_by_id(ids)
        try:
            return render(request,"Restaurantsy/cart.html",{"products":product})
        except:
            return HttpResponseNotFound("<h1>404 error. Page not found!</h1>")

