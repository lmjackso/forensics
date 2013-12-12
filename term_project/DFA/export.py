from xlwt import *
from parser import *

'''
This module is to support the export of metadata parsed with the parser module.

This module is designed to export aforementioned metadata into an excel spreaddsheet format.
'''


def export_metadata(metadata):
	wbk = xlwt.workbook()
	sheet = wbk.add_sheet()
	filenames = metadata.viewkeys()
	filename_ext_list = []
	for filename in filenames:
		filename_ext_list += name_extension_tuple(filename)

	#Get a list of unique file extensions
	unique_exts = []
	for extension in filename_ext_list:
		if extension[1] not in unique_exts:
			unique_exts += [extension[1]]

	#Add new sheet for every unique extension and then add metadata to that sheet
	for extension in unique_exts:
		newsheet = wbk.add_sheet(extension)
		for 