from parser import *

'''
This file contains miscellaneous helper functions that don't belong elsewhere.
'''

def filter_map_by_extension(extension, metadatamap):
  '''
  input str without . extension
  output is map with only files of extension
  '''
  new_map = {}
  for file in metadatamap:
  	if get_extension(file) == extension:
  		new_map[file] = metadatamap[file]
  return new_map