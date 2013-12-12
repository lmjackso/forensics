'''
This module is designed to serve to parse metadata from files into 
an object form that is useable by the framework.
'''
from hachoir_core.error import HachoirError
from hachoir_core.stream import InputIOStream
from hachoir_parser import guessParser
from hachoir_metadata import extractMetadata

from collections import defaultdict
from pprint import pprint

from hachoir_metadata import metadata
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_metadata import *

import os
import sys

def get_file_size(filename):
  return getsize(filename)

def metadata_map(filename):
  filename, realname = unicodeFilename(filename), filename
  parser = createParser(filename)

  # See what keys you can extract
  return metadata.extractMetadata(parser)._Metadata__data

def get_value(metadata_value):
  if metadata_value.values:
    return metadata_value.values[0].value
  return False

def get_text(metadata_value):
  if metadata_value.values:
    return metadata_value.values[0].text
  return False

def create_list(metadata_map):
  keyvalue_list = []
  for k,v in metadata_map.iteritems():
    if v.values:
      keyvalue_list += [get_text(v), get_value(v)]
  return keyvalue_list


'''
def hello(tuple_list)
  # Turn the tags into a defaultdict
  metalist = metadata.extractMetadata(parser, quality=QUALITY_BEST).exportPlaintext()
  meta = defaultdict(defaultdict)
  for item in metalist:
      if item.endswith(':'):
          k = item[:-1]
      else:
          tag, value = item.split(': ')
          tag = tag[2:]
          meta[k][tag] = value

  print meta['Video stream #1']['Image width'] # 320 pixels
'''



def list_to_parse(rootdir):
  list = []
  for root, subFolders, files in os.walk(rootdir):
    list += [root + files]
  return list

def get_extension(filename):
  name, extension = os.path.splittext(filename)
  return extension

def name_extension_tuple(filename):
  file = filename.split('/')
  return [file[-1], get_extension(filename)]

def tuple_list(list):
  tuple_list = []
  for name in list:
    tuple_list += name_extension_tuple(name)
  return tuple_list

def metadata_for_filelike(filelike):
  try:
    filelike.seek(0)
  except (AttributeError, IOError):
    return None
  stream = InputIOStream(filelike, None, tags=[])
  parser = guessParser(stream)
  if not parser:
    return None
  try:
    metadata = extractMetadata(parser)
  except HachoirError:
    return None
  return metadata._Metadata__data

def parse_map_from_directory(directory):
  list_to_be_parsed = list_to_parse(directory)
  parsed_map = {}
  for item in list_to_be_parsed:
    filename = name_extension_tuple(item)[0]
    extension = name_extension_tuple(item)[1]
    metadata = metadata_for_filelike(item)
    parsed_map[filename] = metadata
  return parsed_map


