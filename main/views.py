from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Entry,Customer,Goal
from datetime import datetime
import calendar

@login_required(login_url = 'logoutUser')
def home(request):
    return render(request, 'main/index.html')

def get_stats(request):
    customer = Customer.objects.get(user=request.user)
    entries = Entry.objects.all().filter(customer=customer)
    #print(entries[0].date_created)
    return render(request,'main/stats.html')


def show_calendar(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    month_number = int(list(calendar.month_name).index(month))
    entries = None
    
    if request.method == "POST":
        date_choice = request.POST.get("post_btn")
        customer = request.user.customer #Customer.objects.get(user=request.user)
        entries = Entry.objects.all().filter(customer=customer, date_created = date_choice)
    
    context = {
        "year": year,
        "month":month, 
        "month_number":month_number,
        "cal":calendar.monthcalendar(year,month_number),
        "entries":entries
    }

    return render(request,'main/cal_trial.html',context)

def set_goals(request):
    if request.method == 'POST':
        goal = Goal()
        goal.customer = Customer.objects.get(user=request.user)
        goal.mood = request.POST.get('mood')
        goal.sleep = request.POST.get('sleep')
        goal.screen_time = request.POST.get('screen_time')
        goal.exercise = request.POST.get('exercise')
        goal.steps = request.POST.get('steps')
        goal.relax_time = request.POST.get('chill')
        goal.water = request.POST.get('water')
        goal.save()
        return redirect('goals')
    return render(request, 'main/goals.html')

def entry_page(request):
    return render(request,'main/userinput2.html')

def new_entry(request):
    selection = request.GET.get('selection')
    if selection == None:
        return render(request,"main/userinput2.html")

    values = selection.split(",")
    entry = Entry()
    entry.customer = Customer.objects.get(user=request.user)
    entry.mood = values[0]
    entry.exercise = values[1]
    entry.relax_time = values[2]
    entry.steps = values[3]
    entry.sleep = values[4]
    entry.water = values[5]
    entry.screen_time = values[6]
    entry.save()
    return render(request, 'main/userinput2.html')