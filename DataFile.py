class DataFile(object):
    #Atributos:
    filename = None

    def __init__(self,filename):
        self.filename=filename

    def getFilename(self):
        return self.filename
