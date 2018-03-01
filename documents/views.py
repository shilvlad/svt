# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .models import SvtType, SvtUnit, SvtPeriod
from forms import PeriodForm
#from django import forms
import datetime


# Create your views here.

def start(request):
    docs = SvtPeriod.objects.all()
    context = {'docs':docs}
    return render(request, 'documents/index.html', context)

def load_sap_file(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
            print "SAVED"
        else:
            print "NOT SAVED"
        context = {}
        return render(request, 'documents/index.html', context)
    else:
        form = PeriodForm()

        context = {'form':form, }
        return render(request, 'documents/load_sap_file.html', context)
