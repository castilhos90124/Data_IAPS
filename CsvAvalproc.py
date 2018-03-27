from DataFile import DataFile
from Stactic import Stactic
import os


class CsvAvalproc(DataFile):

    MAX_TABLE_WIDTH = 14

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

    def writeTitleCell(self,title_name):
        self.file.write(title_name + ";")


    def appendData(self,txt_avalproc_data):

        self.image.append(txt_avalproc_data[0])
        self.sam.append(txt_avalproc_data[1])
        self.aval_cycle.append(txt_avalproc_data[2])
        self.aval_sample.append(txt_avalproc_data[3])
        self.aval_rt.append(txt_avalproc_data[5])
        self.aval_resp.append(txt_avalproc_data[6])

    def nextLine(self):
        self.file.write("\n")


    #Retorna true se estourou o limite do array, false caso contrario
    def writeData(self,data_list,initial_index,final_index):
        data_end = False
        for i in range(initial_index,final_index):
            if i < len(data_list):
                self.file.write(data_list[i] + ";")
            else:
                data_end = True
        return data_end

        return

    def write(self):
        data_end = False
        index = 0

        while not data_end :

            self.writeTitleCell("Image:")
            self.writeData(self.image,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("SAM:")
            self.writeData(self.sam,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("Aval. RT:")
            self.writeData(self.aval_rt,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("Aval. Resp:")
            data_end = self.writeData(self.aval_resp,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()
            self.nextLine()
            self.nextLine()

            index = index + self.MAX_TABLE_WIDTH
