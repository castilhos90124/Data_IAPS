from DataFile import DataFile

class TxtIaps(DataFile):

    def __init__(self,filename):
        name = self.validateFilename(filename)
        self.filename = name + ".txt"

    #funçao que varre o header do arquivo txt
    #retorna o arquivo com o "cursor" logo após o header end
    def skipHeader(self,txt_arq):
        return txt_arq
        pass

    #função que tokeniza as informaçoes entre logframe start e end do logframe Avalproc
    #retorna um array com as informaçoes desejadas
    def parseAvalprocLogframe():
        pass

    #função que tokeniza as informaçoes entre logframe start e end do logframe Avalproc
    #retorna um array com as informaçoes desejadas
    def parseAttraprocLogframe():
        pass

    #função que verifica se a procedure é attracproc
    #returna true se for attracproc e false caso contrario
    def isAttractproc():
        pass

    #funçao que escreve no arquivo csv as informaçoes importantes do logframe do Avalproc
    def writeCsvAvalproc():
        pass

    #funçao que escreve no arquivo csv as informaçoes importantes do logframe do Attracproc
    def writeCsvAttractproc():
        pass
