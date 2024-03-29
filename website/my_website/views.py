from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *
from .models import *



def home(request):

    if request.method == 'GET':
        try:
            print(request.GET)
           
            if request.GET['name']:
                message = Request()
                message.name = request.GET['name']
                message.email = request.GET['Email']
                message.description = request.GET['Message']
                message.title = request.GET['Subject']
                message.save()

        except Exception as e:
            print(str(e))
    else:
        print("Error 404")

    return render(request, "index.html" )