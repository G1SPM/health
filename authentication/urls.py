from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register_user,name="registerUser"),
    path('login/',views.login_user,name="loginUser"),
    path('',views.login_user,name="loginUser"),
    path('logout/',views.logout_user,name='logoutUser')
]