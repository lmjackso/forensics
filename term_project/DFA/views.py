#import parser
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response


def single(request):
  context = {}

  #map = parse_map_from_directory(dir)
  return render(request, 'DFA/single.html', context)



def comparison(request):
  context = {}

  #map = parse_map_from_directory(dir)
  return render(request, 'DFA/comparison.html', context)

def export(request):
  context ={}

  return render(request, 'DFA/export.html', context)