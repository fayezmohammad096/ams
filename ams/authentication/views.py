from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
import re
from django.core.mail import send_mail
from django.template.loader import render_to_string #https://docs.djangoproject.com/en/4.2/topics/templates/
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives #https://docs.djangoproject.com/en/4.2/topics/email/
# importing datetime module for now()
import datetime
from cryptography.fernet import Fernet #https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
from . import models


from ams import settings
# Create your views here.
def index(request):
    
    return render(request,'auth/register.html')
# working on 39_2 no videos..........
def store(request):
    if(request.method=='POST'):
        uname = request.POST.get('uname') #collect data from html file
        email = request.POST.get('email') #collect data from html file
        password = request.POST.get('pass') #collect data from html file
        con_pass = request.POST.get('con_pass') #collect data from html file

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        valid = 0
        if(re.fullmatch(regex,email)): #re for regex
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
            admin = models.Admins()
            # using now() to get current time
            current_time = str(datetime.datetime.now())
            v_key = uname+current_time

            key = Fernet.generate_key()
 
            # Instance the Fernet class with the key
 
            fernet = Fernet(key)
            encMessage = fernet.encrypt(v_key.encode())
            encpassword = fernet.encrypt(password.encode())
            v_status = 0
            admin.name=uname
            admin.email = email
            admin.password = encpassword
            admin.v_key = encMessage
            admin.v_status = v_status
            admin.save()
            link = "http://127.0.0.1:8000/register/verification?v_key="+str(encMessage)
            msg = "Check this varification link"
            rendered = render_to_string("auth/reg_email.html", {"content": msg,"link":link})
            text_content = strip_tags(rendered)#remove html content
            email= EmailMultiAlternatives(
                "User Registration",
                text_content,
                settings.EMAIL_HOST_USER,
                [email],
                
            )
            email.attach_alternative(rendered, "text/html")
            email.send()
            return HttpResponse("Success")

