from ast import Or
from msilib.schema import CreateFolder
from multiprocessing import context
from pydoc import pager
from re import A

from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from urllib import request
from django.core.paginator import Paginator
from venv import create
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect ,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404 
from .models import  customuser
from django.views.generic import ListView , DetailView , View
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import  PasswordChangeForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .form import CreateUserForm 
# Create your views here.
from django.contrib.auth.models import User 
# def shop(request):
#     return render(request,'shop.html')
def index(request):
    return render(request, 'home.html')
def logoutuser(request):
    logout(request)
    messages.success(request, ' ขอบคุณที่ใช้บริการ')
    return redirect('../../login')

def loginPage(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        user = authenticate(request, email=email, password=password, username = username)
        if user is not None:
            login(request, user)

            messages.info(request, 'ยินดีต้อนรับสู่ MASTER OF MUSIC' , user)
            return redirect('../../#')
            
        else:
            messages.info(
                request, 'ชื่อผู้ใช้งาน และ รหัสผ่านไม่ถูกต้อง กรุณาเช็คแล้วกรอกใหม่')
    context = {}
    return render(request, 'login.html', context)
def register(request):
    form = CreateUserForm()

    if request.method == 'POST' or request.method == 'FILES':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, ' ขอบคุณที่สมัครสมาชิก : ' + user)
            return redirect('../../login')
        else:
            messages.info(
                request, 'ชื่อผู้ใช้งาน และ รหัสผ่านไม่ถูกต้อง กรุณาเช็คแล้วกรอกใหม่')

    context = {'form': form}
    return render(request, 'register.html', context)


