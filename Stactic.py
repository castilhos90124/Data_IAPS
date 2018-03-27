
class Stactic(object):

    #@staticmethod
    #recebe uma string e a retorna sem espaços e sem caracteres "especiais"
    def clearString(string):
        clean = string.replace(" ","")
        clean = clean.replace("\t","")
        clean = clean.replace("\n","")

        return clean

    def caseUnsensitive(string):
        string = string.upper()
        print(string)
        string = string.lower()
        print(string)

        return string
