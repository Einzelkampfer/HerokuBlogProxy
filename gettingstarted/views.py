import os
from django.http import HttpResponse
import urllib2
import os, sys
import time, datetime
import re
import json
import HTMLParser
from sgmllib import SGMLParser
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def getPageContent(request, postfix="/"):
	url = 'https://zhengsuizhan.blogspot.com/' + postfix + "?m=1"
	content = urllib2.urlopen(url).read()
	content = content.replace("http://zhengsuizhan.blogspot.com/", "http://zhengsuizhan-blogspot.herokuapp.com/")
	content = content.replace("?m=1", "")
	return HttpResponse(content)
