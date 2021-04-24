from django.shortcuts import render, HttpResponse, redirect
from . import customAuth
import requests
from .models import FormModel
from .forms import FormModelForm

# Create your views here.

def index(request):
    return render(request, 'index.html', context={'title':'hello base'})

api_url = "http://lucid.nassa.com.bd/api/Login/GetEmployeeAsync?userName=fazle.rabbi@nassa.com.bd&password=fazle.rabbi@321&moduleId=0"



def fetch_data(request):
    api = api_url
    header = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get(api,header)
    lucid_data = response.json()
    '''
    context = {
        
        "name":lucid_data['UserName'],
        "pass":lucid_data['Password']
    }
    print(context)
    '''
    


    return render(request, 'form.html', {})



def form_data(request):

    api = api_url
    header = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get(api,header)
    lucid_data = response.json()


    if request.method == "GET":
        form = FormModelForm(request.GET)
        if form.is_valid():
            userdata = form.cleaned_data['username']
            passdata = form.cleaned_data['password']

            if userdata in lucid_data["UserName"]:
                status = lucid_data["IsLucidUser"]

                
                return render(request, 'found_user.html',
                context={"user_success":userdata, 
                         "module":status}) 

            

        else:
            form = FormModelForm()
            
    
    return render(request, "form.html", context={"form":form})