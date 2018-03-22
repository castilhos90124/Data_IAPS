from DataFile import DataFile
class CsvIaps(DataFile):
    #Atributos:
    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"
