from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'blog/index.html')  #firsst argument of render is request and second argument of  render is name of template

# Create your views here.
