from django.shortcuts import render, redirect
from pymongo import MongoClient
from .models import ClassArticles

def restaurants(request):
    restaurants = ClassArticles.readAll()
    return render(request, "index.html", {"restaurants": restaurants})

def createRestaurant(request):
    if request.method == "POST":
        Description = request.POST["Description"]
        Info = request.POST["Info"]
        Name = request.POST["Name"]
        ClassArticles.create(Description, Info, Name)
        return redirect("restaurants")
    return render (request, 'create.html')

def editRestaurant(request, Name):
    restaurant = ClassArticles.readByName(Name)
    if request.method == "POST":
        Description = request.POST["Description"]
        Info = request.POST["Info"]
        Name = request.POST["Name"]
        ClassArticles.update(Description, Info, Name)
        return redirect("restaurants")
    return render(request, 'edit.html', {'restaurant': restaurant})

def deleteRestaurant(request, Name):
    ClassArticles.deleteByName(Name)
    return redirect("restaurants")
