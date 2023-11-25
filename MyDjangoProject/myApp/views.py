from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from openai import OpenAI
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


# def welcome(request):
#     return render(request, "index.html")
@login_required
def welcome(request):
    return render(request, "index.html")


@login_required
def aboutus(request):
    return render(request, "about.html")


@login_required
def contactus(request):
    return render(request, "contact.html")


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Change 'welcome' to the name of your welcome page URL
            return redirect(welcome)
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Change 'home' to the name of your home page URL
            return redirect(welcome)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def gpt_process(strVal):

    client = OpenAI(
        api_key="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")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant, you have to give answer correctly and give your answer in a single line minimum."},
            {"role": "user", "content": strVal}
        ]
    )
    return str(completion.choices[0].message.content)


@login_required
def generateNum(request):
    result = None
    gptProcessed = None
    if request.method == "POST":
        myInput = str(request.POST['text'])
        gptProcessed = gpt_process(myInput)
        result = gptProcessed
        myObj = Person(userinputvalue=myInput, mycalvalue=gptProcessed)
        myObj.save()
        # print(mynum)
    return render(request, "generatenum.html", {'result': result})


@never_cache
def logout_view(request):
    logout(request)
    # Your additional logic if any
    return HttpResponse("Logged out successfully"), redirect('login')
