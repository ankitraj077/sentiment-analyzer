import pieap
import piemoto
import piebolt
import piesam
import pieyu
import piexi
from django.shortcuts import render
import nltk

def read_page1():
    pieap.py
    return render(request,'personal/home.html')
def read_page2():
    piemoto.py
    return render(request,'personal/home.html')
def read_page3():
    piebolt.py
    return render(request,'personal/home.html')
def read_page4():
    piesam.py
    return render(request,'personal/home.html')
def read_page5():
    pieyu.py
    return render(request,'personal/home.html')
def read_page6():
    piexi.py
    return render(request,'personal/home.html')

def index(request):
    return render(request,'personal/home.html')
def contact(request):
    return render(request,'personal/basic.html',{'content':['if u waana contact then email','ama@gmail.com']})


'''def request_page(request):
    if(request.GET.get('mybtn')):
        pie.review_read(request)'''
        


