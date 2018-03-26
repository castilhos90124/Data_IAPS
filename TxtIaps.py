from DataFile import DataFile
from Stactic import Stactic

class TxtIaps(DataFile):

    avalproc_data = [""] * 8
    attractproc_data = [""] * 11

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
    #armazena as informaçoes desejadas no self.avalproc_data
    def parseAvalprocLogframe(self):
        word = []
        count = 0
        line = ""
        #self.avalproc_data[0]=""
        self.skipLine()

        #Nesse ponto a proxima linha a ser lida é a da Image: xxxx.jpg

        while line != "***LogFrameEnd***":
            line = self.file.readline()
            word = line.split()
            #print(word)

            self.avalproc_data[count] = word[1]
            count +=1

            line = Stactic.clearString(line)
        #print("\n")


    #função que tokeniza as informaçoes entre logframe start e end do logframe Avalproc
    #retorna um array com as informaçoes desejadas
    def parseAttraprocLogframe(self):
        word = []
        count = 0
        line = ""

        while line != "***LogFrameEnd***":
            line = self.file.readline()
            word = line.split()
            #print(word)
            #print(word[1],"\n")

            self.attractproc_data[count] = word[1]
            count +=1

            line = Stactic.clearString(line)
        #Nesse ponto a proxima linha a ser lida é a Atractivity: x



    #função que verifica se a procedure é attracproc
    #returna true se for attracproc e false caso contrario
    def isAttractproc(self):
        word = []
        line = self.file.readline()
        line = Stactic.clearString(line)
        #print(line)
        if line == "***LogFrameStart***":
            line = self.file.readline()
            word = line.split(" ")
            #print(word)
            #print(word[1])
            word[1] = Stactic.clearString(word[1])
            if word[1] == "attractproc" :
                return True
            else:
                return False
        else:
            print("Erro: funçao isAttractProc chamada na linha errada do txt\n")
            return False



    #funçao que escreve no arquivo csv as informaçoes importantes do logframe do Avalproc
    def writeCsvAvalproc(self):
        pass

    #funçao que escreve no arquivo csv as informaçoes importantes do logframe do Attracproc
    def writeCsvAttractproc(self):
        pass

    def writeCsvAvalprocHeader(self):
        pass

    def writeCsvAttractprocHeader(self):
        pass
