from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html")

def result(request):
    model1=joblib.load('finalised_model.sav')

    lis=[]

    lis.append(request.GET["Solar Zenith Angle"])
    lis.append(request.GET["Wind Direction"])
    lis.append(request.GET["Relative Humidity"])
    lis.append(request.GET["Temperature"])
    lis.append(request.GET["Cloud Type"])
    lis.append(request.GET["Wind Speed"])


    ans=model1.predict([lis])

    return render(request,"result.html",{'ans':ans,'lis':lis})
