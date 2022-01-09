from django.shortcuts import render, redirect
from employee.forms import ProductForm
from employee.models import Product


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
    employees = Product.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Product.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Product.objects.get(id=id)
    employee.delete()
    return redirect("/show")
