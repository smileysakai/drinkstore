from django.shortcuts import render
from .models import Drink
from .forms import DrinkForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "drinks/index.html", {
        "drinks": Drink.objects.all()
    })
    
def drink(request, drink_id):
    drink = Drink.objects.get(pk=drink_id)
    return render(request, "drinks/drink.html", {
        "drink":drink
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
    
    
    
    
    
    'category','name', 'price','description','ingredients','upload'