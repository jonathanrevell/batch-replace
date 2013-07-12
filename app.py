from fileFindAndReplace import *
from fileSystemHelper import *
from csvParser import *
from inputHelper import *
import os
import time

working_dir = getWorkingDirectory()
step_pause_duration = 0.5
def step_pause():
	time.sleep(step_pause_duration)

print("Working directory: " + working_dir)


class App():
	def __init__( self ):
		self.path_csv = None
		self.parser = None
		self.replacement_keys = None
		self.replacer = None
		self.path_run = None
		self.file_list = None
		self.extension = ''


	## LOAD IN THE REPLACEMENT PAIRS
	## Process the CSV file

	def getReplacementKeys( self ):
		self.path_csv = getValidInput("Path of the CSV containing the replacement pairings","Path does not exist. Try again.", validatePath )

		self.parser = csvParser()
		self.parser.setCodec("ISO-8859-1")
		self.parser.setPath(self.path_csv)
		print("Parsing CSV file...")
		self.replacement_keys = self.parser.parseFile()
		step_pause()
		print("Found (" + str( len( self.replacement_keys ) ) + ") keys")
		step_pause()

		if( getConfirmation("Display the keys?") ):
			for key in self.replacement_keys:
				if(len(key) >= 2):
					print( key[0] + ": " + key[1] )




	## CHOOSE TARGET DIRECTORY/FILES
	## Determine which files to run the find and replace operation in

	def chooseTargetDirectory( self ):
		self.replacer = FileFindAndReplace()
		self.replacer.setCodec("ISO-8859-1")

		shouldGetDirectory = True

		while shouldGetDirectory:
			self.path_run = getValidInput("Path of the target directory or file","Path does not exist. Try again.", validatePath)

			self.file_list = []
			self.extension = ''

			if( os.path.isdir(self.path_run) ):
				os.chdir(self.path_run);
				print("Directory contains " + str( len(os.listdir(".")) ) + " files.")
				self.extension = input("Please provide the file extension to use (e.g: txt)")
				
				self.file_list = []
				for _file in os.listdir("."):
					if( _file.endswith("." + self.extension) ):
						self.file_list.append( os.path.join(self.path_run, _file) )

				print("Found " + str( len(self.file_list) ) + " files with the extension: " + self.extension )
				if getConfirmation("List files found?"):
					for _file in self.file_list:
						print("\t" + _file)
			else:
				self.file_list.append(self.path_run)

			if( len(self.file_list) > 0 ):
				shouldGetDirectory = not getConfirmation("Use these files?")





	## FIND AND REPLACE
	## Run the find and replace operation on the selected files

	def runFindAndReplace( self, simulated ):
		shouldRun = True

		while(shouldRun):
			replacements = 0

			if simulated:
				print("Simulating find and replace")
				for _file in self.file_list:
					self.replacer.setPath( _file )
					print("Simulating: " + _file)
					file_replacements = self.replacer.simulatedReplace( self.replacement_keys )
					replacements += file_replacements
					print( str(file_replacements) + " replacements\r" )
					step_pause()

				print("Finished. Simulated (" + str(replacements) + ") replacements.")
				simulated = False
				shouldRun = getConfirmation("Run actual find and replace now?")
			else:
				for _file in self.file_list:
					print("Simulating: " + _file)
					self.replacer.setPath( _file )
					file_replacements = self.replacer.replace( self.replacement_keys )
					replacements += file_replacements
					print( str(file_replacements) + " replacements\r" )
					step_pause()
				shouldRun = False
				print("Finished. Made (" + str(replacements) + ") replacements.")

	def run( self ):
		# Actual process
		continueProcess = True

		while( continueProcess ):
			os.system('cls')
			self.getReplacementKeys()
			self.chooseTargetDirectory()
			self.runFindAndReplace( getConfirmation("Run simulation first?") )

			continueProcess = getConfirmation("Process another batch?")


app = App()
app.run()

