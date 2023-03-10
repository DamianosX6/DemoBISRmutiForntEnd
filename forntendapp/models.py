from cProfile import label
from importlib.metadata import requires
from inspect import classify_class_attrs
from pickle import TRUE
import re
from sre_parse import CATEGORIES
from statistics import mode
from unicodedata import category
from django.db import models
from django.conf import settings
# from django.shortcuts import reverse
from django.urls import reverse
from django.contrib.auth.models import User , AbstractUser , PermissionsMixin ,BaseUserManager,UserManager
from uuid import uuid4
from django.urls import reverse

class customuser(AbstractUser):
     username = models.CharField(max_length=30)
     name = models.CharField(max_length=30)
     surname = models.CharField(max_length=30)
     t_address = models.CharField(max_length=30)
     a_address = models.CharField(max_length=30)
     p_address = models.CharField(max_length=30)
     zipcode = models.CharField(max_length=30)
     tel = models.CharField(max_length=30)
     dateofregis = models.DateField(auto_now=True)
     email = models.EmailField(unique=True)
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)
     last_login = models.TimeField(auto_now=True)
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['username']

     def __str__(self):
        return self.username 


