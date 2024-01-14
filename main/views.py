
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

@login_required(login_url="/")
def thankyou(request):
    form = ClienThankyouForm(request.POST or None)
    if form.is_valid():
        try:
            userclient = Client.objects.get(username=form["username"].value())
            userid = userclient.id
            
            send_mail(
                "Email subject is here", 
                thankyoumsg(form['first_name'].value(), form['last_name'].value(), form['username'].value(), userid ,form['phone_number'].value()),
                "wealthyonlinecoachig@gmail.com",
                [form["email"].value(),], 
            )
            return redirect('home')
        
        except Client.DoesNotExist:
            form.add_error("Matching User doesnt exist")
            
    context = {}
    context["form"] = form
    return render(request, "thankyou.html", context)
    
    
