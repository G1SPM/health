from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Entry


@login_required(login_url = 'logoutUser')
def add_entry(request):
    if request.method == 'POST':
        entry = Entry()
        entry.customer = request.user.customer
        entry.mood = request.POST.get('mood')
        entry.sleep = request.POST.get('sleep')
        """entry.screen_time = request.POST.get('screen_time')
        entry.exercise = request.POST.get('exercise')
        entry.steps = request.POST.get('steps')
        entry.relax_time = request.POST.get('relax_time')
        entry.water = request.POST.get('water')"""
        entry.save()
        return redirect('home')
    return render(request, 'main/test.html')

