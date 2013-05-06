from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
import os
import cql
import datetime

def hello(request):    
    return HttpResponse("Hello Del bold")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def my_view(request):
    now = datetime.datetime.now()
    fp = open('/Users/Del/Desktop/mushrooms/mushrooms/media/mushroomsWeb/index.html')
    t = Template(fp.read())
    fp.close()
    con = cql.connect('localhost', 9160,'demo', cql_version='3.0.0')
    cursor = con.cursor()
    #CQLString = "create columnfamily t1 (okey int primary key, observer varchar, image varchar)"
    #x=cursor.execute(CQLString)
    
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
def field(request):
    now = datetime.datetime.now()
    fp = open('/Users/Del/Desktop/mushrooms/mushrooms/media/mushroomsField/index.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
def market(request):
    now = datetime.datetime.now()
    fp = open('/Users/Del/Desktop/mushrooms/mushrooms/media/mushroomsMarket/index.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
def mushroomBook(request):
    now = datetime.datetime.now()
    fp = open('/Users/Del/Desktop/mushrooms/mushrooms/media/mushroomsFieldMushroomBook/index.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)