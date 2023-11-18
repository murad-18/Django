from openai import OpenAI
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
