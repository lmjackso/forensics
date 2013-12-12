from parser import *
from helper import *
from export import *
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response


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


