# Create your views here.

from hachoir_core.error import HachoirError
from hachoir_core.stream import InputIOStream
from hachoir_parser import guessParser
from hachoir_metadata import extractMetadata

from collections import defaultdict
from pprint import pprint

from hachoir_metadata import metadata
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hacoir_metadata.metadata_item import *

import os
import sys


def metadata_map(filename):
  filename, realname = unicodeFilename(filename), filename
  parser = createParser(filename)

  # See what keys you can extract
  return metadata.extractMetadata(parser, quality=QUALITY_BEST)._Metadata__data

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
    return metadata
