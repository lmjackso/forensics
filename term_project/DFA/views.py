#import parser
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response


def home(request):
  context = {}
 # map = parse_map_from_directory(dir)
  return render(request, 'DFA/twographs.html', context)