from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Entry,Customer,Goal

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
    return render(request, 'main/index.html')

def get_stats(request):
    customer = Customer.objects.get(user=request.user)
    entries = Entry.objects.all().filter(customer=customer)
    #print(entries[0].date_created)
    return render(request,'main/stats.html')

def show_calendar(request):
    date_choice = "2023-04-03"
    if request.method == "POST":
        customer = request.user.customer #Customer.objects.get(user=request.user)
        entries = Entry.objects.all().filter(customer=customer, date_created = date_choice)
        context = {"entries":entries}

        return render(request,'main/test.html',context)
    return render(request,'main/test.html')

def set_goals(request):
        if request.method == 'POST':
            goal = Goal()
            goal.customer = Customer.objects.get(user=request.user)
            goal.mood = request.POST.get('mood')
            goal.sleep = request.POST.get('sleep')
            goal.screen_time = request.POST.get('screen_time')
            goal.exercise = request.POST.get('exercise')
            goal.steps = request.POST.get('steps')
            goal.relax_time = request.POST.get('relax_time')
            goal.water = request.POST.get('water')
            goal.save()
            return redirect('goals')
        return render(request, 'main/goals.html')

