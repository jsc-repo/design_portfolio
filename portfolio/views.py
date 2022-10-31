from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Image
from .forms import ContactForm

# Create your views here.
def home(request):
    image = Image.objects.all()

    return render(request, 'portfolio/home.html', {'images': image})



def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subject']
            surname = form.cleaned_data['surname']
            from_email = form.cleaned_data['from_email']
            msg = form.cleaned_data['msg']
            try:
                send_mail(name, surname, from_email, msg, ['choijs1@outlook.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, 'portfolio/home.html' ,{'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')