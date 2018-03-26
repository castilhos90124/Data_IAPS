from DataFile import DataFile
from Stactic import Stactic

class CsvAttractproc(DataFile):
    #Atributos:
    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"

    
    def writeAttractprocTitles(self):
        pass
