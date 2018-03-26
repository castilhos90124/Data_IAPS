from DataFile import DataFile
from Stactic import Stactic

class CsvIaps(DataFile):
    #Atributos:
    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"

    def writeAvalprocTitles():
        pass

    def writeAttractprocTitles():
        pass
