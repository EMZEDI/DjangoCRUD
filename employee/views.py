from django.shortcuts import render, redirect
from employee.forms import ProductForm
from employee.models import Product


def intro(request):
    prodc = Product.objects.all()
    return render(request, 'intro.html', {'prodc': prodc})


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    prod = Product.objects.all()
    return render(request, "show.html", {'prods': prod})


def edit(request, id):
    prod = Product.objects.get(id=id)
    return render(request, 'edit.html', {'prod': prod})


def update(request, id):
    prod = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('/show')

    return render(request, 'edit.html', {'prod': prod})


def destroy(request, id):
    prod = Product.objects.get(id=id)
    prod.delete()
    return redirect('/show')
