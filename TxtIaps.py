from DataFile import DataFile

class TxtIaps(DataFile):
    #Atributos:
    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".txt"
