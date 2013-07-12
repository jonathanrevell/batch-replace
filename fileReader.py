import os
import codecs


class FileReader:
  def __init__( self ):
    self.hasOpenFile = False      # Whether the file is currently open
    self.handle = None            # The handle to the file being read
    self.path = ""                # The full path of the file being read
    self.lineNumber = -1          # The current line number in the file
    self.hasValidHandle = False   # Whether the handle to the file is valid
    self.codec = None             # Some files require special codecs to parse
  
  # Opens a new file
  def open( self, path ):
    self.setPath( path )
    return self.__open()

  def setPath( self, path ):
    self.close()
    self.path = path
    self.hasOpenFile = False
    self.hasValidHandle = False

  def setCodec( self, codec ):
    self.close()
    self.codec = codec

  def isOpen( self ):
    return self.hasOpenFile

  # Re-opens the file that was previously opened
  def reopen( self ):
    if( self.hasOpenFile ):
      self.close()
    if( self.hasValidHandle ):
      return self.__open()
    else:
      return self.open( self.path )

  # Closes the open handle
  def close( self ):
    if( self.hasValidHandle and self.hasOpenFile ):
      self.handle.close()
      self.hasOpenFile = False

  #Gets the next line in an open file
  def getNextLine( self ):
    if( self.hasOpenFile ):
      eof = False           #Indicates End of File (eof)
      line = self.handle.readline()

      if(line == ''):
        eof = True
        self.close()
      else:
        self.lineNumber += 1
    else:
      eof = True
      line = ''

    return eof, line, self.lineNumber

  ### Private Functions ###
  #Actually opens the file
  def __open( self ):
    if(self.hasOpenFile):
      self.close()

    if( os.path.exists(self.path) ):
      if(self.codec == None):
        self.handle = open( self.path, 'r' )
      else:
        self.handle = codecs.open( self.path, 'r', self.codec)

      self.lineNumber = 0
      self.hasOpenFile = True
      self.hasValidHandle = True
      return True
    else:
      return False