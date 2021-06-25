from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail     #-->send_mail is a function that allows us to send an E-mail with the respective settings. 
from django.shortcuts import render, HttpResponse

# Create your views here.
# from sendemail.models import 
from .models import Newsletter
def newsletter(request):
    if request.method=="POST":
         email = request.POST.get("email")
         emaillist = Newsletter(email=email)
         emaillist.save()

     #     send_mail(subject, message, from_email, to_list, fail_silently=True)
         subject = 'Your Sinup is Completed'
         message = 'Thankyou you for sining up to our Newsletter :)'
         from_email = settings.EMAIL_HOST_USER 
         to_list = [emaillist.email]

         send_mail(subject,message,from_email,to_list, fail_silently=False)

         return render(request, 'index.html')
    
    return render(request, 'index.html')


