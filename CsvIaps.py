from DataFile import DataFile
class CsvIaps(DataFile):
    #Atributos:
    def __init__(self,filename):
        self.filename = filename + ".csv"
