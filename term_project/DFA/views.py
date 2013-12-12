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

  if request.method == 'GET':

    options = []
    path = os.getcwd()
    os.chdir(path+"/DFA/static/options")
    for f in glob.glob("*.js"):
      #options.append(f.strip('.js'))
      options.append(f)

    os.chdir(path)
    context['options'] = options
    return render(request, 'DFA/index.html', context)

  if request.method == 'POST':
    values = [1, 2, 3]
    key = "hi"

    data = [{'key':key, 'values':values}]
    data_json = json.dumps(data)
    context['data_json'] = json.dumps(data)
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


