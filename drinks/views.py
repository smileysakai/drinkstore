from django.shortcuts import render
from .models import Drink
from .forms import DrinkForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from decimal import *
from django.db.models import Sum
#from _overlapped import NULL
# Create your views here.
def index(request):
    #del request.session['cart']
    if 'cart' not in request.session:
            request.session['cart'] = {}
    else:
        cart_total_price=0
        for key, value in request.session['cart'].items():
            cart_total_price += Decimal(value['total_price'])
    return render(request, "drinks/index.html", {
        "drinks": Drink.objects.all(),
        "cart":request.session['cart'],
        "cart_total_price":str(cart_total_price)
    })
    
def drink(request, drink_id):
    drink = Drink.objects.get(pk=drink_id)
    cart_total_price=0
    for key, value in request.session['cart'].items():
        cart_total_price += Decimal(value['total_price'])
    return render(request, "drinks/drink.html", {
        "drink":drink,
        "cart":request.session['cart'],
        "cart_total_price":str(cart_total_price)
    })
    
def add(request):
    if request.method=="POST":
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            drink = Drink(category=form.cleaned_data['category'], name=form.cleaned_data['name'], price=form.cleaned_data['price'], description=form.cleaned_data['description'], ingredients=form.cleaned_data['ingredients'], upload=request.FILES['upload'])
            drink.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "drinks/add.html",{
                "form": form
            })
    
    return render(request, "drinks/add.html",{
            'form': DrinkForm()
    })
    
#Shopping cart using sessions
def add_to_cart(request, drink_id):
    if request.method=="POST":
        drink = Drink.objects.get(pk=drink_id)
        name = drink.name
        price= drink.price
        quantity= request.POST['quantity']
        total_price = price * Decimal(quantity)
        order={
            'name':name,
            'price':str(price),
            'quantity':quantity,
            'total_price':str(total_price)
        }
        request.session['cart'][drink_id] = order
        request.session.modified = True
        return HttpResponseRedirect(reverse("index"))
    
    #passing the below render to the view_cart html
    #return render(request, "drinks/drink.html", {
    #    "drink":drink,
    #    #for the cart
    #    "cart" : request.session['cart']
    #    #"message":request.session['cart'][1]
    #})
    #return HttpResponseRedirect(reverse("drink", args=(drink.id,)))
    #return render(request, "drinks/index.html", {
    #"message": request.session['cart'][drink_id]
    #})
       
#not using a particular view atm
def view_cart(request):    
    if 'cart' not in request.session:
            request.session['cart'] = {}
    cart_total_price=0
    cart_total_quantity=0
    for key, value in request.session['cart'].items():
        cart_total_price += Decimal(value['total_price'])
        #cart_total_quantity += int(value['quantity'])
    return render(request, "drinks/view_cart.html", {
        "cart":request.session['cart'],
        #"cart_total_quantity":str(cart_total_quantity),
        "cart_total_price":str(cart_total_price),
        #"test":str(cart_total_quantity) + "this string here" + str(cart_total_price)
        #"test":Decimal(request.session['cart']['1']['total_price'])+Decimal(request.session['cart']['2']['total_price'])
        #"test":request.session['cart']['2']
        #found out that the 2nd argument in the comment above must be string
    })

def delete_cartitem(request, drink_id):
    if request.method=="POST":
        del request.session['cart'][str(drink_id)]
        request.session.modified = True
    return HttpResponseRedirect(reverse("view_cart"))

def update_cartitem(request, drink_id):
    if request.method=="POST":
        quantity=request.POST['quantity']
        total_price = Decimal(request.session['cart'][str(drink_id)]['price']) * Decimal(quantity)
        request.session['cart'][str(drink_id)]['quantity']=quantity
        request.session['cart'][str(drink_id)]['total_price']=str(total_price)
        request.session.modified = True
    return HttpResponseRedirect(reverse("view_cart"))

#def checkout(request):
    # Creating Access Token for Sandbox
   # client_id = "AZci21POXG3JTRRsL0Lt_FY2m43muEA36bKYKOvATmhRmiNfWqOtG_JV3RJymqtjrIKTL2-9nw_R844k"
   # client_secret = "EDdNNU3blvqbb17wT7S_djKxXEsmz2f-B5qK70H_ZBb2rvPgiZE7FaXFmdhEmZejGutZApNcNaj2qxOk"
    # Creating an environment
   # environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
   # client = PayPalHttpClient(environment)






