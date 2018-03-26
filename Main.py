from TxtIaps import TxtIaps
from CsvIaps import CsvIaps
from Stactic import Stactic

import os




def main():

    filename = input("Entre com o nome do arquivo\n")

    txt = TxtIaps(filename)
    csv_avalproc = CsvIaps(filename + "_Avalproc")
    csv_attractproc = CsvIaps(filename + "_Attractproc")

    #print(f"txt name: {txt.getFilename()}")
    #print(f"csv_avalproc name: {csv_avalproc.getFilename()}")
    #print(f"csv_attractproc name: {csv_attractproc.getFilename()}")


    txt.file = open(txt.getFilename(), "r", encoding="utf-16-le")
    csv_avalproc.file = open(csv_avalproc.getFilename(), "w")
    csv_attractproc.file = open(csv_attractproc.getFilename(), "w")

    txt.skipHeader()
    #print(f"na main, txt readline: {txt.file.readline()}")

    #txt.skipLine()
    #print(f"na main, txt readline: {txt.file.readline()}")

    while Stactic.clearString(txt.file.readline()) == "Level:2" :

        if txt.isAttractproc() :
            #print("entrou no if")
            txt.parseAttraprocLogframe()

            txt.writeCsvAttractproc()
        else:
            #print("entrou no else")
            txt.parseAvalprocLogframe()


            txt.writeCsvAvalproc()
    print(txt.avalproc_data)
    print(txt.attractproc_data)

    txt.file.close()
    csv_avalproc.file.close()

main()
