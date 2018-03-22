from TxtIaps import TxtIaps
from CsvIaps import CsvIaps



def main():

    filename = input("Entre com o nome do arquivo\n")

    txt = TxtIaps(filename)
    csv = CsvIaps(filename)


    print(f"txt name:{txt.getFilename()}")
    print(f"csv name:{csv.getFilename()}")



main()
