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





    #return
    while Stactic.clearString(txt.file.readline()) == "Level:2" :

        if txt.isAttractproc() :
            #print("entrou no if")
            txt.parseAttraprocLogframe()

            #txt.writeCsvAttractproc()
        else:
            #print("entrou no else")
            txt.parseAvalprocLogframe()

            csv_avalproc.appendData(txt.avalproc_data)

            #csv_avalproc.write()


    #print(txt.avalproc_data)
    #print(txt.attractproc_data)

    #print(f"\n{csv_avalproc.image}")
    #print(f"\n{csv_avalproc.sam}")
    #print(f"\n{csv_avalproc.aval_cycle}")
    #print(f"\n{csv_avalproc.aval_sample}")
    #print(f"\n{csv_avalproc.aval_rt}")
    #print(f"\n{csv_avalproc.aval_resp}")

    csv_avalproc.write()

    txt.file.close()
    csv_avalproc.file.close()
    csv_attractproc.file.close()

main()
