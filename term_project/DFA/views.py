from parser import *
from helper import *
from export import *
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response


def home(request):
  context = {}
  dir = "/Users/lmjackso/CMU/15-498/forensics/term_project/test_data"
  map = parse_map_from_directory(dir)
  return render(request, 'DFA/index.html', context)

def export(request):
  directory = request.GET['directory']
  export_metadata(parse_map_from_directory(directory), request.GET['exportname'])
  return redirect('/')