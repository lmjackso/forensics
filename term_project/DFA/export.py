import xlwt
import xlrd
import os
from parser import *

'''
This module is to support the export of metadata parsed with the parser module.

This module is designed to export aforementioned metadata into an excel spreaddsheet format.
'''


def export_metadata(metadata, newname):
	wbk = xlwt.Workbook()
	filenames = metadata.viewkeys()
	filename_ext_list = []
	for filename in filenames:
		filename_ext_list += [name_extension_tuple(filename)]
	#Get a list of unique file extensions
	rows = {}
	unique_exts = []
	for extension in filename_ext_list:
		if extension[1] not in unique_exts:
			unique_exts += [extension[1]]
			rows[extension[1]] = 0

	#Add new sheet for every unique extension and then add metadata to that sheet
	for extension in unique_exts:
		newsheet = wbk.add_sheet(extension)#, cell_overwrite_ok=True)
		for name in filename_ext_list:
			#Add file to sheet of same file extension.
			if name[1] == extension:
				col = 0
				if rows[extension] == 0:
					tmpcol = 1
					for namen in metadata[name[0]].viewkeys():
						if namen in metadata[name[0]] and metadata[name[0]][namen]:
							newsheet.write(rows[extension], tmpcol, namen)
							tmpcol += 1
					rows[extension] +=1
				#Add new column for each data type
				for data in metadata[name[0]].viewkeys():
					print name[0]
					if rows[extension] != 0:
						if col == 0:
							newsheet.write(rows[extension], col, name[0])
							col += 1
						if data in metadata[name[0]] and metadata[name[0]][data]:
							newsheet.write(rows[extension], col, str(get_value(metadata[name[0]][data])))
							col += 1
				rows[extension] += 1
	wbk.save(newname)