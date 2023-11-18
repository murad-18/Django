from django.shortcuts import render
from .models import Person
# Create your views here.


# def welcome(request):
#     return render(request, "index.html")
def welcome(request):
    return render(request, "index.html")


def aboutus(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contact.html")


def generateNum(request):
    result = None
    if request.method == "POST":
        mynum = int(request.POST['number'])
        result = mynum*125
        myObj = Person(userinputvalue=mynum, mycalvalue=result)
        myObj.save()
        print(mynum)
    return render(request, "generatenum.html", {'result': result})
