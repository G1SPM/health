from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

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
    max_score = MaxValueValidator(10)
    min_score = MinValueValidator(0)

    #create all entries
    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null=True)
    title = models.CharField(max_length=500,null = True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    mood = models.PositiveSmallIntegerField(validators=[min_score,max_score],null=True)
    sleep = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    screen_time = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    exercise = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    steps = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    relax_time = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)
    water = models.IntegerField(default = 0,validators=[min_score,max_score],null=True)

    def __str__(self):
        return self.title

    
class Goal(models.Model):
    max_score = MaxValueValidator(10)
    min_score = MinValueValidator(0)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    overall_mood = models.IntegerField(default = 0,validators=[min_score,max_score])
    sleep_quality = models.IntegerField(default = 0,validators=[min_score,max_score])
    steps = models.IntegerField(default = 0,validators=[min_score,max_score])
    water = models.IntegerField(default = 0,validators=[min_score,max_score])

    def __str__(self):
        return Customer.first_name