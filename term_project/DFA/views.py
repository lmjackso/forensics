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
			
		file_list = list_to_parse(directory)
  		files_to_parse =[]
  		for file in file_list:
  			if file.split('/')[-1][0] != '.':
  				files_to_parse.append(file)
		list_dir = list_to_parse(directory)
		map_dir = parse_map_from_directory(directory)
		
		if(method == 'us_map'):
			key = 'location'
			for fileName in files_to_parse:
				lat = get_value(parse_map_from_directory(directory)[fileName]['latitude'])
				long = get_value(parse_map_from_directory(directory)[fileName]['longitude'])
				values.push([lat,long])
		
		elif(method == 'edge'):
			key = 'creation'
			for fileName in files_to_parse:
				time = get_value(parse_map_from_directory(directory)[fileName]['creation_date'])
				values.push([time,fileName])
		elif(metatype == 'file_size'):
			key = 'file_size'
			for fileName in files_to_parse:
				file = fileName.split("/")
				fileName = file[-1]
				lat = get_value(map_dir[fileName]['latitude'])
				long = get_value(map_dir[fileName]['longitude'])
				values.append([lat,long])
			
		
		elif(method == 'edge'):
			key = 'creation'
			for fileName in list_dir:
				file = fileName.split("/")
				fileName = file[-1]
				time = get_value(map_dir[fileName]['creation_date'])
				values.append([time,fileName])
		elif(metatype == 'file_size'):
			key = 'file_size'
			for fileName in files_to_parse:
				size = get_file_size(fileName)
				values.append(size)
		else:
			key = metatype
			for fileName in files_to_parse:
				temp = get_value(parse_map_from_directory(directory)[fileName][metatype])
				values.push(temp)
			for fileName in list_dir:
				file = fileName.split("/")
				fileName = file[-1]
				temp = get_value(map_dir[fileName][metatype])
				values.append(temp)
    
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


