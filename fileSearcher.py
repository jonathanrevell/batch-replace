from fileReader import *

class FileSearcher:
  def __init__( self, path ):
    self.path = path
    self.reader = FileReader()
    self.reader.setPath( path )
    self.searchTerm = None
    self.__resetResults()

  def findAll( self, searchFor ):
    self.reader.reopen()
    self.__resetResults()
    self.searchTerm = searchFor
    eof = False

    while( not eof ):
      eof, hasMatch, line, lineNum = self.checkNextLine()
      if( hasMatch ):
        self.__saveResult( line, lineNum )

    return self.results


  def checkNextLine( self ):
    hasMatch = False
    if( self.reader.isOpen() ):
      eof, line, lineNum = self.reader.getNextLine()
      if( not eof ):
        if( line.find( self.searchTerm ) != -1 ):
          hasMatch = True
    else:
      eof = True
      line = ''
      lineNum = -1

    return eof, hasMatch, line, lineNum

  def __resetResults( self ):
    self.results = []

  def __saveResult( self, line, lineNum ):
    result = line, lineNum
    self.results.append( result );