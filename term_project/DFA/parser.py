# Create your views here.

from hachoir_core.error import HachoirError
from hachoir_core.stream import InputIOStream
from hachoir_parser import guessParser
from hachoir_metadata import extractMetadata


import os
import sys

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
