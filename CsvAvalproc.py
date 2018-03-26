from DataFile import DataFile
from Stactic import Stactic

class CsvAvalproc(DataFile):
    #Atributos:
    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"

    def writeAvalprocTitles(self):
        self.file.write("anderson;\nlorenzo;")
        pass
