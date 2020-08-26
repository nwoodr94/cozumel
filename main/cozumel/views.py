from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
import os

def index(request):
    template = loader.get_template('cozumel/index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('cozumel/about.html')
    return HttpResponse(template.render())

def itinerary(request):
    template = loader.get_template('cozumel/itinerary.html')
    return HttpResponse(template.render())

def gallery(request):
    os_path = r'/home/nwoodr94/code/cozumel/main/cozumel/static/cozumel/images/'
    django_path = r'../../static/cozumel/images/'

    images = os.listdir(os_path)

    paths = []
    for image in images:
        paths += [django_path + image]

    first_element = paths[0]

    context = {"paths": paths, "first_element": first_element}
    template = loader.get_template('cozumel/gallery.html')

    return HttpResponse(template.render(context, request))

import pandas as pd

def reservations(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            date_range = pd.date_range(start_date, end_date)

            for date in date_range:
                print(date.strftime("%Y-%m-%d"))

    form = ReservationForm()

    context = {"form": form}

    template = loader.get_template('cozumel/reservations.html')

    return HttpResponse(template.render(context, request))



class ReservationForm(forms.Form):

    start_date = forms.DateField(label="Check-In 📅", widget=forms.DateInput(attrs={'type': 'text', 'class': 'form-control'}))
    end_date = forms.DateField(label="Check-Out 📅", widget=forms.DateInput(attrs={'type': 'text', 'class': 'form-control'}))

import datetime

def test(request):
    today = datetime.date.today()
    date = today.strftime("%Y, %m, %d")
    print(date)
    return HttpResponse(date)