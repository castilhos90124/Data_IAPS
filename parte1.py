nome_arq = input('Entre com o nome do arquivo\n')
nome_arq = nome_arq.replace('.txt','')
entrada = open(nome_arq + '.txt','r',encoding='utf-16-le')
saida = open(nome_arq + '.csv','w')
header = open('Header.txt','w',encoding='utf-16-le')

linha =''

while linha != '*** Header End ***\n':
    linha = entrada.readline()
    header.write(linha)

header.close()

linha = entrada.readline()
palavras = linha.split()
count = 0
for i in palavras:
    palavras[count] = palavras[count].replace(' ','')
    palavras[count] = palavras[count].replace('\t','')
    palavras[count] = palavras[count].replace('\n','')
    count = count + 1

if palavras[0] == 'Level:':
    old_level = palavras[1]

    while entrada.readline():
        variaveis = []
        linha = ''
        campos = []
        while linha != '*** LogFrame End ***':
            linha = entrada.readline()
            linha = linha.replace('\t','')
            linha = linha.replace('\n','')
            aux = linha.split(':')
            if aux[0] != '*** LogFrame End ***':
                aux[1] = aux[1].replace(' ','')
                variaveis.append(aux[0])
                aux2 = []
                aux2.append(aux[1])
                campos.append(aux2)

        new_level = old_level
        
        while new_level == old_level:
            linha = entrada.readline()
            palavras = linha.split()
            count = 0
            for i in palavras:
                palavras[count] = palavras[count].replace(' ','')
                palavras[count] = palavras[count].replace('\t','')
                palavras[count] = palavras[count].replace('\n','')
                count = count + 1
            if palavras:
                if palavras[0] == 'Level:':
                    new_level = palavras[1]
                    if new_level == old_level:
                        entrada.readline()
                        linha = ''
                        count = 0
                        while linha != '*** LogFrame End ***':
                            linha = entrada.readline()
                            linha = linha.replace('\t','')
                            linha = linha.replace('\n','')
                            aux = linha.split(':')
                            if aux[0] != '*** LogFrame End ***':
                                aux[1] = aux[1].replace(' ','')
                                campos[count].append(aux[1])
                                count = count + 1
            else:
                new_level = -1
                
        for i in range(int(old_level) - 1):
            saida.write(';')
        saida.write('Level;' + old_level + '\n')

        count = 0
        for i in variaveis:
            for j in range(int(old_level) - 1):
                saida.write(';')
            saida.write(i)
            saida.write(';')
            for j in campos[count]:
                saida.write(j)
                saida.write(';')
            count = count + 1
            saida.write('\n')
        old_level = new_level
        saida.write('\n')
        nome_para_DT = open('NomeArq.txt','w')
        nome_para_DT.write(nome_arq + '.csv')
        nome_para_DT.close()
    
else:
    erro = open('Erro.txt','w',encoding='utf-16-le')
    erro.write('Documento de entrada não está correto\n')
    erro.close()

entrada.close()
saida.close()


