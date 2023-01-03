from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def dashboard_page(request):
    return render(request, 'dashboard/dashboard.html', {})

def upload_page(request):
    return render(request, 'dashboard/upload.html', {})