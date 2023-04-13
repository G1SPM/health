from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.first_name

class Entry(models.Model):
    #set the max and min scores for any entry
    max_score = MaxValueValidator(5)
    min_score = MinValueValidator(0)

    
    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    date_created = models.DateField(auto_now_add = False, null=True, default=datetime.date.today)
    #create all entries
    title = models.CharField(max_length=500,null = True, default="hello")
    description = models.CharField(max_length=1000,null=True,blank=True)
    mood = models.PositiveSmallIntegerField(default = 0, validators=[min_score,max_score],null=True)
    sleep = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    screen_time = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    exercise = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    steps = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    relax_time = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    water = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)

    def __str__(self):
        return self.title

    
class Goal(models.Model):
    max_score = MaxValueValidator(5)
    min_score = MinValueValidator(0)

    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    mood = models.PositiveSmallIntegerField(default = 0, validators=[min_score,max_score],null=True)
    sleep = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    screen_time = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    exercise = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    steps = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    relax_time = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    water = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)

    def __str__(self):
        return self.customer.first_name