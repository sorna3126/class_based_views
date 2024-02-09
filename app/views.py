from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.
def fbv(request):
    return HttpResponse('Function Based Views')

class cbv(View):
    def get(self,request):
        return HttpResponse('Class Based Views')


# rendering of html page by FBV
def fbvhtml(request):
    return render(request,'fbvhtml.html')

# rendering of html page by CBV
class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')

# inserting data through function based views
def insert_data_fbv(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('School is created By FBV')
    return render(request,'insert_data_fbv.html',d)

# inserting data through class based views
class insert_data_cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_data_cbv.html',d)

    def post(self,request):
        
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('school is inserted by CBV')

class cbv_template(TemplateView):
    template_name='cbv_template.html'