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

    txt.skipLine()
    #print(f"na main, txt readline: {txt.file.readline()}")

#while !eof :
    if txt.isAttractproc() :
        txt.parseAttraprocLogframe()
        txt.writeCsvAttractproc()
    else:
        txt.parseAvalprocLogframe()
        txt.writeCsvAvalproc()



main()
