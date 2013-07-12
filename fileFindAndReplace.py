# Class that finds and replaces lines
# Based on: http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python

from fileReader import *

from tempfile import mkstemp
from shutil import move
from os import remove, close

class FileFindAndReplace(FileReader):

	def replace(self, replacement_keys):
		#Create temp file
		replacement_count = 0
		fh, abs_path = mkstemp()
		new_file = open(abs_path,'w')

		self.reopen()

		line_num = 0
		for line in self.handle:
			line_num += 1
			for pair in replacement_keys:
				if(len(pair) >= 2):
					replacement_count += line.count(pair[0])
					line = line.replace(pair[0], pair[1])
			new_file.write(line)

		#close temp file
		new_file.close()
		close(fh)
		self.handle.close()

		#Remove original file
		remove(self.path)

		#Move new file
		move(abs_path, self.path)

		return replacement_count


	def simulatedReplace(self, replacement_keys):
		#Create temp file
		replacement_count = 0
		self.reopen()

		line_num = 0
		for line in self.handle:
			line_num += 1
			for pair in replacement_keys:
				if(len(pair) >= 2):
					replacement_count += line.count(pair[0])
					line = line.replace(pair[0], pair[1])

		#close temp file
		self.handle.close()

		return replacement_count		