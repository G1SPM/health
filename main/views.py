from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Entry,Customer,Goal
from datetime import datetime,timedelta,date
import calendar

@login_required(login_url = 'logoutUser')
def home(request):
    return render(request, 'main/index.html')

def chart(request):
    # Get the data for the last 7 days
    end_date = date.today()
    start_date = end_date - timedelta(days=6)
    entries = Entry.objects.filter(date_created__range=[start_date, end_date]).order_by('date_created')

    # Prepare the data for the chart
    mood_values = [entry.mood for entry in entries]
    sleep_values = [entry.sleep for entry in entries]
    exercise_values = [entry.exercise for entry in entries]
    steps_values = [entry.steps for entry in entries]
    water_values = [entry.water for entry in entries]
    chill_values = [entry.relax_time for entry in entries]
    screen_values = [entry.screen_time for entry in entries]
    dates = [entry.date_created.strftime('%m/%d') for entry in entries]

    # Render the template with the chart data
    context = {'mood_values': mood_values, 
               'sleep_values': sleep_values, 
               'exercise_values': exercise_values, 
               'steps_values': steps_values, 
               'water_values': water_values, 
               'chill_values': chill_values, 
               'screen_values': screen_values,
               'labels': dates}
    return render(request, 'main/stats.html', context)


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