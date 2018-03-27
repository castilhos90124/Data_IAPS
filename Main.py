from TxtIaps import TxtIaps
from CsvAttractproc import CsvAttractproc
from CsvAvalproc import CsvAvalproc
from Stactic import Stactic

import os




def main():

    error = False
    completed = False

    while error or not completed:
        os.system("CLS")
        error = False
        completed = False

        filename = input("Entre com o nome do arquivo\n")

        txt = TxtIaps(filename)
        csv_avalproc = CsvAvalproc(filename + "_Avalproc")
        csv_attractproc = CsvAttractproc(filename + "_Attractproc")



        try:
            txt.file = open(txt.getFilename(), "r", encoding="utf-16-le")
        except:
            print("Nome de arquivo incorreto !\n")
            os.system("PAUSE")
            error = True

        if not error:

            try:
                csv_avalproc.file = open("Tabelas/" + csv_avalproc.getFilename(), "w")
                csv_attractproc.file = open("Tabelas/" + csv_attractproc.getFilename(), "w")

            except:
                os.mkdir("Tabelas")
                csv_avalproc.file = open("Tabelas/" + csv_avalproc.getFilename(), "w")
                csv_attractproc.file = open("Tabelas/" + csv_attractproc.getFilename(), "w")


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

            os.system("CLS")

            print("Arquivos gravados com sucesso\n")
            choice = input("Deseja inserir outro arquivo .txt ? (s/n)\n")

            choice = choice.lower()
            if choice == "s":
                completed = False
            else:
                completed = True

main()
