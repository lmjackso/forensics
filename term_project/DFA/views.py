from parser import *
from helper import *
from export import *
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
import glob
import os


import json

def home(request):

  context={}
  values = []
  options = []
  path = os.getcwd()
  os.chdir(path+"/DFA/static/options")
  for f in glob.glob("*.js"):
    options.append(f.strip('.js'))
      # options.append(f)

  os.chdir(path)
  context['options'] = options


  if request.method == 'GET':
    return render(request, 'DFA/index.html', context)

  if request.method == 'POST':
    if 'directory' in request.POST and request.POST['directory']:
      directory = request.POST['directory']
      print directory

    if 'method' in request.POST and request.POST['method']:
      method = request.POST['method']
      print method

    if 'type' in request.POST and request.POST['type']:
      metatype = request.POST['type']
      print metatype

	if(method == 'us_map'):
		key = 'location'
		for fileName in list_to_parse(directory):
			lat = get_value(parse_map_from_directory(directory)[fileName]['latitude'])
			long = get_value(parse_map_from_directory(directory)[fileName]['longitude'])
			values.push([lat,long])
	
	elif(method == 'edge'):
		key = 'creation'
		for fileName in list_to_parse(directory):
			time = get_value(parse_map_from_directory(directory)[fileName]['creation_date'])
			values.push([time,fileName])
	elif(metatype == 'file_size'):
		key = 'file_size'
		for fileName in list_to_parse(directory):
			size = get_file_size(fileName)
			values.push(size)
	else:
		key = metatype
		for fileName in list_to_parse(directory):
			temp = get_value(parse_map_from_directory(directory)[fileName][metatype])
			values.push(temp)
    
    # send name of graph representation method
    name = method
    graphname = method + 'graph'

    data = [{'key':key, 'values':values}]
    data_json = json.dumps(data)
    context['name'] = name
    context['graphname'] = graphname
    context['jsonData'] = data_json
    context['data'] = data
    return render(request, 'DFA/index.html', context)

def single(request):
  context = {}
  dir = "/Users/lmjackso/CMU/15-498/forensics/term_project/test_data"
  map = parse_map_from_directory(dir)
  return render(request, 'DFA/single.html', context)

def export(request):
  context = {}
  if not 'directory' in request.GET or not request.GET['directory']:
    return render(request, 'DFA/export.html', {'error': 'You incorrectly entered the directory!'})
  if not 'exportname' in request.GET or not request.GET['exportname']:
    return render(request, 'DFA/export.html', {'error': 'You incorrectly entered the directory!'})  

  directory = request.GET['directory']
  export_metadata(parse_map_from_directory(directory), request.GET['exportname'])
  return render(request, 'DFA/export.html', context)


def comparison(request):
  context = {}

  #map = parse_map_from_directory(dir)
  return render(request, 'DFA/comparison.html', context)


