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




main()
