from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
import re
# Create your views here.
def index(request):
    # template = loader.get_template("auth/register.htlml")
    return render(request,'auth/register.html')

def store(request):
    if(request.method=='POST'):
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        con_pass = request.POST.get('con_pass')
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        valid = 0
        if(re.fullmatch(regex,email)):
            valid = 1
        else:
            valid = 0
        if((len(uname)==0) or (len(email)==0) or (len(password)==0) or (len(con_pass)==0)):
            return HttpResponse("The field can't empty")
        elif(password!=con_pass):
            return HttpResponse("Password does not match")
        elif(valid==0):
            return HttpResponse("Email is not valid")
        else:
            return HttpResponse("Success")

