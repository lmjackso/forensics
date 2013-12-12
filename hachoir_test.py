from collections import defaultdict
from pprint import pprint

from hachoir_metadata import metadata
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser

import re

# using this example 
filename = 'Bobs.Burgers.s03e01.Ear-sy.Rider.mkv' 
filename, realname = unicodeFilename(filename), filename
parser = createParser(filename)

# See what keys you can extract
for k,v in metadata.extractMetadata(parser)._Metadata__data.iteritems():
	if v.values:
		print v.key, v.values[0].value
	#else:
	#	print k, v.key, v.values

# Turn the tags into a defaultdict
metalist = metadata.extractMetadata(parser).exportPlaintext()
meta = defaultdict(defaultdict)
for item in metalist:
	if item.endswith(':'):
		k = item[:-1]
	else:
		tag, value = item.split(': ',1)
		tag = tag[2:]
		meta[k][tag] = value
		print k, tag

for k in meta:
	if(re.match(r'^File', k) != None):
		print meta[k]['File size']
#print meta['Metadata']['Creation date']
#print meta['Metadata']['MIME type']