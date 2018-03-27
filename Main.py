from TxtIaps import TxtIaps
from CsvAttractproc import CsvAttractproc
from CsvAvalproc import CsvAvalproc
from Stactic import Stactic

import os




def main():

    filename = input("Entre com o nome do arquivo\n")

    txt = TxtIaps(filename)
    csv_avalproc = CsvAvalproc(filename + "_Avalproc")
    csv_attractproc = CsvAttractproc(filename + "_Attractproc")


    txt.file = open(txt.getFilename(), "r", encoding="utf-16-le")
    csv_avalproc.file = open(csv_avalproc.getFilename(), "w")
    csv_attractproc.file = open(csv_attractproc.getFilename(), "w")


    txt.skipHeader()

    #return
    while Stactic.clearString(txt.file.readline()) == "Level:2" :

        if txt.isAttractproc() :

            txt.parseAttraprocLogframe()
            csv_attractproc.appendData(txt.attractproc_data)

        else:

            txt.parseAvalprocLogframe()
            csv_avalproc.appendData(txt.avalproc_data)


    csv_avalproc.write()
    csv_attractproc.write()

    txt.file.close()
    csv_avalproc.file.close()
    csv_attractproc.file.close()

main()
