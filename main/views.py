from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Entry,Customer


@login_required(login_url = 'logoutUser')
def add_entry(request):
    if request.method == 'POST':
        entry = Entry()
        entry.customer = Customer.objects.get(user=request.user)
        entry.mood = request.POST.get('mood')
        entry.sleep = request.POST.get('sleep')
        entry.screen_time = request.POST.get('screen_time')
        entry.exercise = request.POST.get('exercise')
        entry.steps = request.POST.get('steps')
        entry.relax_time = request.POST.get('relax_time')
        entry.water = request.POST.get('water')
        entry.save()
        return redirect('home')
    return render(request, 'main/test.html')

def get_stats(request):
    customer = Customer.objects.get(user=request.user)
    entries = Entry.objects.all().filter(customer=customer)
    print(entries[0].date_created)
    return render(request,'main/stats.html')

def show_calendar(request):
    date_choice = "2023-03-31"
    #if(request.method == 'POST'):
    customer = Customer.objects.get(user=request.user)
    entries = Entry.objects.all().filter(customer=customer, date_created = date_choice)
    print(f"entry c: {entries}")
    return render(request,'main/calendar.html')

