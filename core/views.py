from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http.response import StreamingHttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
import json
import os
import sys
import time
import pandas as pd
import sys
sys.path.append('./core')
from list_database import lists
from user_database import users
from step_database import steps

users = users()
lists = lists()
steps = steps()

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))

def order(request):
    template = loader.get_template('orders.html')
    return HttpResponse(template.render({}, request))

def detail(request):
    recipe_name = str(request.GET.get('name'))
    global lists
    details = lists.get_recipe_detail(recipe_name)
    global steps
    recipe_step = steps.get_recipe_detail(recipe_name, 'html')
    context = {
        'recipe_name' : recipe_name,
        'list_name' : details[0],
        'recipe_description' : details[1],
        'photo_path' : details[2],
        'total_time' : details[3],
        'calories' : details[4],
        'recipe_step' : recipe_step,
    }
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(context, request))

def index(request):
    global lists
    lists_name = lists.get_listnames()
    list_chosen = request.GET.get('list_chosen')
    if list_chosen == None:
        list_transfer = lists.get_full_list()
        name_display = 'Welcome using the recipe management system!'
    else:
        list_transfer = lists.search(list_chosen, 'list_name')
        name_display = list_chosen
    template = loader.get_template('index.html')
    context = {
        'list_transfer' : list_transfer,
        'lists_name' : lists_name,
        'name_display' : name_display,
    }
    return HttpResponse(template.render(context, request))



def search(request):
    content = request.POST.get('searchcontent')
    option = request.POST.get('option')
    global lists
    lists_name = lists.get_listnames()
    result = lists.search(content, option)
    template = loader.get_template('index.html')
    context = {
        'list_transfer' : result,
        'lists_name' : lists_name,
        'name_display' : 'Search Result',
    }
    return HttpResponse(template.render(context, request))

def edit(request):
    template = loader.get_template('edit_2.html')
    return HttpResponse(template.render({}, request))

def edit_2(request):
    recipe_name = request.GET.get('name')
    global lists
    details = lists.get_recipe_detail(recipe_name)
    global steps
    recipe_step = steps.get_recipe_detail(recipe_name, 'js')
    if recipe_name != None:
        context = {
            'status' : True,
            'recipe_name' : recipe_name,
            'list_name' : details[0],
            'recipe_description' : details[1],
            'photo_path' : details[2],
            'total_time' : details[3],
            'calories' : details[4],
            'recipe_step' : recipe_step
        }
    else:
        context = {
            'status' : False,
        }
    
    template = loader.get_template('edit.html')
    response = HttpResponse(template.render(context, request))
    response.set_cookie('recipe_name',recipe_name)
    return response


def add(request):
    list_name = request.POST.get('list_name')
    recipe_name = request.POST.get('recipe_name')
    recipe_description = request.POST.get('recipe_description')
    total_time = request.POST.get('total_time')
    calories = request.POST.get('calories')
    creator_name= request.COOKIES.get('username')
    global steps
    global lists
    lists.add_recipe(list_name, recipe_name, total_time, recipe_description, calories, creator_name)
    i = 1
    while(request.POST.get('step_description_' + str(i)) != None):
        step_description = request.POST.get('step_description_' + str(i))
        j=0
        while(request.POST.getlist('ingredient_' + str(j))!=None):
          ingredient = request.POST.getlist('ingredient_' + str(j))
          quantity = request.POST.getlist('quantity_' + str(j))
          unit = request.POST.getlist('unit_' + str(j))
          steps.add_step(recipe_name, i, ingredient, quantity, unit, step_description)
          j+=1
        i += 1
    return HttpResponseRedirect("/detail?name=" + recipe_name)


def add_delete(request):
    global steps
    global lists
    k=request.COOKIES.get('recipe_name')
    creator_name= request.COOKIES.get('username')
    lists.delete_list(k)
    steps.delete_step(k)
    list_name = request.POST.get('list_name')
    recipe_name = request.POST.get('recipe_name')
    recipe_description = request.POST.get('recipe_description')
    total_time = request.POST.get('total_time')
    calories = request.POST.get('calories')
    lists.add_recipe(list_name, recipe_name, total_time, recipe_description, calories,creator_name)
    i = 0
    while(request.POST.get('step_description_' + str(i)) != None):
        step_description = request.POST.get('step_description_' + str(i))
        j=0
        while(request.POST.getlist('ingredient_' + str(j))!=None):
          ingredient = request.POST.getlist('ingredient_' + str(j))
          quantity = request.POST.getlist('quantity_' + str(j))
          unit = request.POST.getlist('unit_' + str(j))
          steps.add_step(recipe_name, i, ingredient, quantity, unit, step_description)
          j+=1
        i += 1
    return HttpResponseRedirect("/detail?name=" + recipe_name)


def register(request):
    name = str(request.POST.get('signup-name'))
    robot_id = str(request.POST.get('robotID'))
    email = str(request.POST.get('signup-email'))
    password = str(request.POST.get('signup-password'))
    record = {'name':name, 'email':email, 'password':password, 'robot_id':robot_id}
    global users
    users.append(record)
    response = HttpResponseRedirect("/index/")
    response.set_cookie('name',name)
    response.set_cookie('robot_id',robot_id)
    response.set_cookie('email', email)
    return response




def validate(request):
    global users
    email = request.POST.get('signin-email')
    password = request.POST.get('signin-password')
    if users.login(email, password):
        response = HttpResponseRedirect("/index/")
        response.set_cookie('name',users.username(email))
        response.set_cookie('email',email)
        response.set_cookie('robot_id',users.robot_id(email))
        return response
    else:
        response = HttpResponseRedirect("/")
        return response
        

def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render({}, request))

def logout(request):
    response= HttpResponseRedirect('/')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('robot_id')
    return response


def manage_data(request):
    template = loader.get_template('account1.html')
    return HttpResponse(template.render({}, request))

def change_data(request):
    name = str(request.POST.get('change_name'))
    robot_id = str(request.POST.get('change_robotid'))
    password = str(request.POST.get('change_password'))
    email=request.COOKIES['email']
    users.update(name,password,robot_id,email)
    return HttpResponseRedirect('/')



