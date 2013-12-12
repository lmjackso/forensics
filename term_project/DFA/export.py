from xlwt import *
from parser import *

'''
This module is to support the export of metadata parsed with the parser module.

This module is designed to export aforementioned metadata into an excel spreaddsheet format.
'''


def export_metadata(metadata, newname):
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
		for name in filename_ext_list:
			row = 0
			#Add file to sheet of same file extension.
			if name[1] == extension:
				col = 0
				if row == 0:
					tmpcol = 1
					for name in metadata[name[0]]:
						newsheet.write(row, tmpcol, name)
						tmpcol += 1
				#Add new column for each data type
				for data in metadata[name[0]]:
					if col == 0:
						newsheet.write(row, col, name[0])
						col += 1
					newsheet.write(row, col, str(metadata[name[0]][data]))
					col += 1
				row += 1
	wbk.save(newname)