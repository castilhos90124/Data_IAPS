from DataFile import DataFile
from Stactic import Stactic
import os


class CsvAvalproc(DataFile):
    #Atributos:
    image = []
    sam = []
    aval_cycle = []
    aval_sample = []
    aval_rt = []
    aval_resp = []


    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"

    def writeTitles(self):
        
        pass

    def appendData(self,txt_avalproc_data):

        self.image.append(txt_avalproc_data[0])
        self.sam.append(txt_avalproc_data[1])
        self.aval_cycle.append(txt_avalproc_data[2])
        self.aval_sample.append(txt_avalproc_data[3])
        self.aval_rt.append(txt_avalproc_data[5])
        self.aval_resp.append(txt_avalproc_data[6])
