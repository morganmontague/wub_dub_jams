from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, Menu_ItemSerializer, CategorySerializer, CuisineSerializer
from pprint import pprint
from .models import Menu_Item, Category, Cuisine, Ingredients
from django.forms.models import model_to_dict
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.
