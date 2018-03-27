from DataFile import DataFile
from Stactic import Stactic
import os


class CsvIAPS(DataFile):

    MAX_TABLE_WIDTH = 14


    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"

    def writeTitleCell(self,title_name):
        self.file.write(title_name + ";")

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

        
