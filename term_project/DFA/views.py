from parser import *
from helper import *
from export import *
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
# Needed to manually create HttpResponses or raise an Http404 exception
from django.http import HttpResponse, Http404
import glob
import os
import datetime
import json
from django.conf import settings, os

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

		list_dir = list_to_parse(directory)
		map_dir = parse_map_from_directory(directory)
		
		if(method == 'us_map'):
			key = 'location'
			for fileName in list_dir:
				if fileName is not None:
					testfile = fileName.split("/")
					fileName = testfile[-1]
					if fileName != ".DS_Store":
						try:
							lat = get_value(map_dir[fileName]['latitude'])
							lon = get_value(map_dir[fileName]['longitude'])
							values.append([lat,lon])
						except(err):
							print "no location found"
			
		elif(method == 'edge'):
			key = 'creation'
			for fileName in list_dir:
				if fileName is not None:
					testfile = fileName.split("/")
					fileName = testfile[-1]
					if fileName != ".DS_Store":

						time = get_value(map_dir[fileName]['creation_date'])
						if time is not None:
							time = time.strftime('%Y-%m-%d %H:%M:%S')
							values.append([time,fileName])
					
		elif(metatype == 'file_size'):
			key = 'file_size'
			for fileName in list_dir:
				if fileName is not None:
					size = get_file_size(fileName)
					values.append(size)
		elif(metatype == 'creation_date'):
			key = metatype
			for fileName in list_dir:
				if fileName is not None:

					testfile = fileName.split("/")
					fileName = testfile[-1]
					print "this is the filename = " + fileName
					if fileName != ".DS_Store":
						time = get_value(map_dir[fileName]['creation_date'])
						if time is not None:
							time = time.strftime('%Y-%m-%d %H:%M:%S')
							values.append(time)
				
		else:
			key = metatype
			for fileName in list_dir:
				if(fileName is not None):
					testfile = fileName.split("/")
					fileName = testfile[-1]
					if fileName != ".DS_Store":

						temp = get_value(map_dir[fileName][metatype])
						values.append(temp)
		
		# send name of graph representation method
		name = method
		graphname = method + 'graph'

		data = [{'key':key, 'values':values}]
		#print data
		data_json = json.dumps(data)
		context['name'] = name
		context['graphname'] = graphname
		context['jsonData'] = data_json
		context['data'] = data
		#return render(request, 'DFA/edge.html', context)
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

#This function is solely meant to pass on the JSON file. 
def retrieveJSON(request):
	context = {}
	backup_path = os.path.join(settings.PROJECT_ROOT, "json_templates", "uss.json")
	return HttpResponse(open(backup_path, 'r'),content_type = 'application/json; charset=utf8')
