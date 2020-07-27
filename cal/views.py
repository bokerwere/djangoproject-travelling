from django.shortcuts import render
from  django.http import  HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html",{"name":"joseph"})
    #return HttpResponse("Hello World",)

def add(request):
    val1= float(request.POST['nam1'])
    val1=float(request.POST['nam2'])
    res=val1+val1

    return render(request,"result.html",{"result":res})