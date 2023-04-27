from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('stats/',views.get_stats,name="stats"),
    #path('calendar/',views.show_calendar,name="calendar"),
    path('goals/',views.set_goals, name='goals'),
    path('entry/',views.entry_page, name="entry"),
    path('new_entry/',views.new_entry, name='new_entry'),
    path('calendar/',views.show_calendar, name="calendar"),
    path('calendar/<int:year>/<str:month>/',views.show_calendar, name="calendar")
]