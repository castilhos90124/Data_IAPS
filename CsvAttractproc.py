from DataFile import DataFile
from Stactic import Stactic
import os


class CsvAttractproc(DataFile):

    MAX_TABLE_WIDTH = 14

    #Atributos:
    attractivity = []
    stimulus = []
    cycle = []
    sample = []
    offset_time = []
    start_time = []
    click_time = []
    vas_res = []
    vas_rt = []


    def __init__(self,filename):

        name = self.validateFilename(filename)
        self.filename = name + ".csv"

    def writeTitleCell(self,title_name):
        self.file.write(title_name + ";")


    def appendData(self,txt_attractproc_data):

        self.attractivity.append(txt_attractproc_data[0])
        self.stimulus.append(txt_attractproc_data[1])
        self.cycle.append(txt_attractproc_data[3])
        self.sample.append(txt_attractproc_data[4])
        self.offset_time.append(txt_attractproc_data[5])
        self.start_time.append(txt_attractproc_data[6])
        self.click_time.append(txt_attractproc_data[7])
        self.vas_res.append(txt_attractproc_data[8])
        self.vas_rt.append(txt_attractproc_data[9])

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

            self.writeTitleCell("Attractivity:")
            self.writeData(self.attractivity,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("StimulusA:")
            self.writeData(self.stimulus,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("Cycle:")
            self.writeData(self.cycle,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("Sample:")
            data_end = self.writeData(self.sample,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("OffsetTime:")
            data_end = self.writeData(self.offset_time,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("StartTime:")
            data_end = self.writeData(self.start_time,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("ClickTime:")
            data_end = self.writeData(self.click_time,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("VAS Res:")
            data_end = self.writeData(self.vas_res,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("VAS RT:")
            data_end = self.writeData(self.vas_rt,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.nextLine()
            self.nextLine()

            index = index + self.MAX_TABLE_WIDTH
