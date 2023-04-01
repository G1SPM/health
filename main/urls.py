from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.add_entry,name="home"),
    path('stats/',views.get_stats,name="stats"),
    path('calendar/',views.show_calendar,name="calendar"),
]