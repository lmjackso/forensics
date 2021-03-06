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
  return os.path.getsize(filename)

def metadata_map(filename):
  filename, realname = filename, filename
  test= filename.split('/')
  if test[-1][0]==u'.' or test[-1][0] == '.':
    return None
  parser = createParser(filename)

  # See what keys you can extract
  if parser:
    return metadata.extractMetadata(parser)._Metadata__data
  return None

def get_value(metadata_value):
  if metadata_value.values:
    return metadata_value.values[0].value
  return None

def get_text(metadata_value):
  if metadata_value.values:
    return metadata_value.values[0].text
  return None

def create_list(metadata_map):
  keyvalue_list = []
  for k,v in metadata_map.iteritems():
    if v.values:
      keyvalue_list.append([k, get_value(v)])
  return keyvalue_list


def list_to_parse(rootdir):
  list = []
  for root, subFolders, files in os.walk(rootdir):
    for file in files:
      list += [root +'/'+ file]
  return list

def get_extension(filename):
  name, extension = os.path.splitext(filename)
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
  print list_to_be_parsed
  parsed_map = {}
  for item in list_to_be_parsed:
    filename = name_extension_tuple(item)[0]
    extension = name_extension_tuple(item)[1]
    metadata = metadata_map(item)
    if metadata:
      parsed_map[filename] = metadata
    print filename
    print extension
  return parsed_map


