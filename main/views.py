from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = 'main')
def homepage(request):
    #return render(request,'main/index.html')
    if request.method == 'POST':
        value = request.POST.get('value')
        # Replace the print() call with your own code to handle the value.
        print("Button " + value + " was clicked!")
        return HttpResponse("Value received: " + value)
    return render(request, 'main/index.html')

def button_view(request):
    print("hello")
