from fileReader import *

class csvParser(FileReader):

	def parseFile(self):
		table = []
		self.reopen()

		for line in self.handle:
			table.append( line.split(',') )

		self.close()
		return table