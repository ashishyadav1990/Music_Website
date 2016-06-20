from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import View
import os


def HomePageView(ListView):
	songs = os.listdir("C:\Users\yadav\Desktop\Music Website\Songs")
	return render_to_response("home.html",{"songs":songs})
