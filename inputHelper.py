import os

def validatePath( path ):
	return os.path.exists( path )

def getValidInput( prompt, invalidPrompt, validator ):
	valid = False
	result = None

	while( not valid ):
		result = input(prompt + ": ")
		valid = validator( result )
		if (not valid):
			print(invalidPrompt)

	return result

def isYes( value ):
	value = value.lower()
	if( value == "y" or value == "yes"):
		return True
	else:
		return False

def getConfirmation( prompt ):
	result = input(prompt + " (y or yes): ")
	return isYes( result )