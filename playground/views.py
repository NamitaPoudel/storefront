from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x

#request handler
def say_hello(request):
    x = calculate()
    #return HttpResponse("Hello, world!!")
    return render(request,'hello.html',{
        'name': 'Namita'
    })