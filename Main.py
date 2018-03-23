from TxtIaps import TxtIaps
from CsvIaps import CsvIaps




def main():

    filename = input("Entre com o nome do arquivo\n")

    txt = TxtIaps(filename)
    csv = CsvIaps(filename)
    #print(f"txt name: {txt.getFilename()}")
    #print(f"csv name: {csv.getFilename()}")

    txt.file = open(txt.getFilename(), "r", encoding="utf-16-le")
    csv.file = open(csv.getFilename(), "w")

    txt.skipHeader()
    #print(f"na main, txt readline: {txt.file.readline()}")

    #txt.skipLine()
    #print(f"na main, txt readline: {txt.file.readline()}")

    while txt.clearString(txt.file.readline()) == "Level:2" :
        #print("entrou no wile")
        if txt.isAttractproc() :
            #print("entrou no if")
            txt.parseAttraprocLogframe()

            txt.writeCsvAttractproc()
        else:
            #print("entrou no else")
            txt.parseAvalprocLogframe()


            txt.writeCsvAvalproc()
    print(txt.avalproc_data)


main()
