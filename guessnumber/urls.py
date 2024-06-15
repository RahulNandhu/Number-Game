from django.urls import path
from . import views

app_name='GuessNumber'

urlpatterns = [
    path('',views.Guess,name='guess')
]