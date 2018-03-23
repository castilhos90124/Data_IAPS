from DataFile import DataFile

class TxtIaps(DataFile):

    def __init__(self,filename):
        name = self.validateFilename(filename)
        self.filename = name + ".txt"

    #funçao que varre o header do arquivo txt
    #retorna o arquivo com o "cursor" logo após o header end
    def skipHeader(self):
        linha = self.file.readline()
        #print(linha)
        #if linha == "*** Header Start ***" :    # bug
        while linha != "*** Header End ***\n" :
            linha = self.file.readline()


    #função que tokeniza as informaçoes entre logframe start e end do logframe Avalproc
    #retorna um array com as informaçoes desejadas
    def parseAvalprocLogframe(self):

        pass

    #função que tokeniza as informaçoes entre logframe start e end do logframe Avalproc
    #retorna um array com as informaçoes desejadas
    def parseAttraprocLogframe(self):
        pass

    #função que verifica se a procedure é attracproc
    #returna true se for attracproc e false caso contrario
    def isAttractproc(self):
        word = []
        line = self.file.readline()
        line = self.clearString(line)
        #print(line)
        if line == "***LogFrameStart***":
            line = self.file.readline()
            word = line.split(" ")
            #print(word)
            #print(word[1])

            if word[1] == "attractproc" :
                return True
            else:
                return False
        else:
            print("Erro: funçao isAttractProc chamada na linha errada do txt\n")
            return False


    #recebe uma string e a retorna sem espaços e sem caracteres "especiais"
    def clearString(self,string):
        clean = string.replace(" ","")
        clean = clean.replace("\t","")
        clean = clean.replace("\n","")

        return clean

    #funçao que escreve no arquivo csv as informaçoes importantes do logframe do Avalproc
    def writeCsvAvalproc(self):
        pass

    #funçao que escreve no arquivo csv as informaçoes importantes do logframe do Attracproc
    def writeCsvAttractproc(self):
        pass
