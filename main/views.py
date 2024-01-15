
from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm, ClienThankyouForm
from .emailtemplates import thankyoumsg
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


def contactme(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        #send_mail(
         #   "this email contains information about registered users", 
          #  f"this user {form['username'].value()} was susccessfully registed into the database.",
           # "wealthyonlinecoachig@gmail.com",
            #["marwane.rako@gmail.com"], 
        # )
        return redirect('home')
    context = {}
    context["form"] = form
    return render(request, "contact.html", context)

@login_required
def thankyou(request):
    form = ClienThankyouForm(request.POST or None)
    if form.is_valid():
        if Client.objects.filter(username=form.cleaned_data["username"]).exists():
            userclient = Client.objects.get(username=form.cleaned_data["username"])
            userid = userclient.id
            
            send_mail(
                "Email subject is here", 
                thankyoumsg(form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['username'], userid ,form.cleaned_data['phone_number']),
                "wealthyonlinecoachig@gmail.com",
                [form["email"].value(),], 
            )
            return redirect('home')
        else:
            form.save()
            userclient = Client.objects.get(username=form.cleaned_data["username"])
            userid = userclient.id
            send_mail(
                "Email subject is here", 
                thankyoumsg(form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['username'], userid ,form.cleaned_data['phone_number']),
                "wealthyonlinecoachig@gmail.com",
                [form["email"].value(),], 
            )
            return redirect('home')
            
    context = {}
    context["form"] = form
    return render(request, "thankyou.html", context)
    
    
