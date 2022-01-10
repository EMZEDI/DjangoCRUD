import mimetypes
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from employee.forms import ProductForm
from employee.models import Product
import pandas as pd


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


def download_all(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.DataFrame(Product.objects.all().values())
    df.reset_index(inplace=True)
    df.to_csv('output.csv', index=False)
    filename = "output.csv"
    filepath = BASE_DIR + "/output.csv"
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


def download_all_file(request):
    # Load the template
    return render(request, 'all.html')


def download_single_file(request, id):
    prod = Product.objects.get(id=id)
    # Load the template
    return render(request, 'single.html', {'prod': prod})


def download_single(request, id):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.DataFrame(Product.objects.all().values())
    df = df[df['id'] == id]
    df.reset_index(inplace=True)
    df.to_csv("file" + str(id) + "_data.csv", index=False)
    filename = "file" + str(id) + "_data.csv"
    filepath = BASE_DIR + "/" + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='csv')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
