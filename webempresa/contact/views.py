from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #suponemos que todo fue bien, redireccionamos
            #return redirect(reverse('contact')+"?ok")
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera : Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no_contestar@inbox.mailtrap.io",
                ["checelesti@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?Error")
                

    return render(request,"contact/contact.html",{'form':contact_form})