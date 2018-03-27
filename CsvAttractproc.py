from CsvIAPS import CsvIAPS
from Stactic import Stactic
import os


class CsvAttractproc(CsvIAPS):



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


    #Retorna true se estourou o limite do array, false caso contrario


    def write(self):
        data_end = False
        index = 0

        while not data_end :

            self.writeTitleCell("StimulusA:")
            self.writeData(self.stimulus,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("VAS.Res:")
            data_end = self.writeData(self.vas_res,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.writeTitleCell("VAS.EstimatedRT:")
            data_end = self.writeData(self.vas_rt,index, index + self.MAX_TABLE_WIDTH)
            self.nextLine()

            self.nextLine()
            self.nextLine()

            index = index + self.MAX_TABLE_WIDTH
