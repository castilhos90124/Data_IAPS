from DataFile import DataFile

class TxtIaps(DataFile):
    #Atributos:
    def __init__(self,filename):
        self.filename = filename + ".txt"
