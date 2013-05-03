from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
import os
import datetime

def hello(request):    
    return HttpResponse("Hello Del bold")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def my_view(request):
    now = datetime.datetime.now()
    now1 = "del42"
    fp = open('/Users/Del/Desktop/mushrooms/mushrooms/index.html')
    t = Template(fp.read())
    fp.close()
    con = cql.connect('localhost', 9160,'demo', cql_version='3.0.0')
    cursor = con.cursor()
    #CQLString = "create columnfamily observation1 (okey int primary key, observer varchar, image varchar)"
    #x=cursor.execute(CQLString)
    template_values = {
            'current_date': now,
            'today': now1,
    }
    html = t.render(Context({dict(template_values)}))
    return HttpResponse(html)