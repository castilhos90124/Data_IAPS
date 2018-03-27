import math
import os
clear = lambda: os.system('cls')

def is_float(valor):
	try:
	    float(valor)
	    return True
	except ValueError:
	    return False

def media(valores):
    if valores:
        soma = 0
        for i in valores:
            soma = soma + float(i)
        return soma/float(len(valores))

def calc_media(tabelas,variavel,bit_dscnsdr_acc_zero):
    for i in tabelas:
        gravar = False
        indices_acc_zero = []
        if bit_dscnsdr_acc_zero:
            if any(s == ACC for s in i[0]):
                index = i[0].index(ACC)
                count = 0
                for j in i[1][index]:
                    if int(j) == 0:
                        indices_acc_zero.append(count)
                    count = count + 1
        if indices_acc_zero:
            if any(s == variavel for s in i[0]) and not any(s == 'Media_' + variavel + '_sem_ACC_zero' for s in i[0]):
                index = i[0].index(variavel)
                soma = 0
                count = 0
                count2 = 0
                for j in i[1][index]:
                    if not any(s == count for s in indices_acc_zero):
                        soma = soma + float(j)
                        count2 = count2 + 1
                    count = count + 1
                _media = soma/float(count2)
                gravar = True
        elif any(s == variavel for s in i[0]) and not any(s == 'Media_' + variavel for s in i[0]):
            index = i[0].index(variavel)
            _media = media(i[1][index])
            gravar = True
        if gravar:
            string = 'Media_' + variavel
            if bit_dscnsdr_acc_zero:
                string = string + '_sem_ACC_zero'
            i[0].append(string)
            media_list=[]
            _media = str("{0:.2f}".format(float(_media)))
            media_list.append(_media)
            i[1].append(media_list)
    return tabelas

def variancia(valores):
    _media = media(valores)
    soma = 0
    _variancia = 0

    for valor in valores:
        soma += math.pow((float(valor) - _media),2)
    _variancia = soma / float(len(valores))
    return _variancia

def desvio_padrao(valores):
    return math.sqrt(variancia(valores))

def calc_DP(tabelas,variavel,bit_dscnsdr_acc_zero):
    for i in tabelas:
        gravar = False
        indices_acc_zero = []
        if bit_dscnsdr_acc_zero:
            if any(s == ACC for s in i[0]):
                index = i[0].index(ACC)
                count = 0
                for j in i[1][index]:
                    if int(j) == 0:
                        indices_acc_zero.append(count)
                    count = count + 1
        if indices_acc_zero:
            if any(s == variavel for s in i[0]) and not any(s == 'DP_' + variavel + '_sem_ACC_zero' for s in i[0]):
                index = i[0].index(variavel)
                soma = 0
                count = 0
                count2 = 0
                for j in i[1][index]:
                    if not any(s == count for s in indices_acc_zero):
                        soma = soma + float(j)
                        count2 = count2 + 1
                    count = count + 1
                _media = soma/float(count2)
                soma = 0
                for valor in i[1][index]:
                    soma += math.pow((float(valor) - _media),2)
                _variancia = soma / float(count2)
                DP = math.sqrt(_variancia)
                gravar = True
        elif any(s == variavel for s in i[0]) and not any(s == 'DP_' + variavel for s in i[0]):
            index = i[0].index(variavel)
            DP = desvio_padrao(i[1][index])
            gravar = True
        if gravar:
            string = 'DP_' + variavel
            if bit_dscnsdr_acc_zero:
                string = string + '_sem_ACC_zero'
            i[0].append(string)
            DP_list=[]
            DP = str("{0:.2f}".format(float(DP)))
            DP_list.append(str(DP))
            i[1].append(DP_list)
    return tabelas

def sum_acertos(variavel,tabelas):
    for i in tabelas:
        soma = 0
        if any(s == variavel for s in i[0]) and not any(s == 'SomaACC' for s in i[0]):
            index = i[0].index(variavel)
            for j in i[1][index]:
                soma = soma + int(j)
            i[0].append('SomaACC')
            soma_list=[]
            soma_list.append(str(soma))
            i[1].append(soma_list)
    return(tabelas)

def media_acertos(variavel,tabelas):
    for i in tabelas:
        if any(s == variavel for s in i[0]) and not any(s == 'MediaACC' for s in i[0]):
            index = i[0].index(variavel)
            _media = str(media(i[1][index]))
            _media = str("{0:.2f}".format(float(_media) * 100))
            i[0].append('MediaACC')
            media_list = []
            media_list.append(_media)
            i[1].append(media_list)
    return(tabelas)

def salva_arq_em_ed(nome_arq):
    entrada = open(nome_arq,'r')
    tabelas = []
    levels = []
    linha = entrada.readline()
    while linha:
        variaveis = []
        campos = []
        tupla = linha.split(';')
        while linha != '' and linha != '\n':
            count = 0
            tam = len(tupla)
            for i in range(tam):
                if tupla[count] == '' or tupla[count] == '\n':
                    tupla.pop(count)
                else:
                    count = count + 1
            if tupla:
                aux = tupla.pop(0)
                if aux != '\n' and aux != 'Level':
                    variaveis.append(aux)
                    vals = []
                    tam = len(tupla)
                    for i in range(tam):
                        vals.append(tupla.pop(0))
                    campos.append(vals)
                elif aux == 'Level':
                    level = tupla.pop()
                    level = level.split('\n')
                    levels.append(level.pop(0))
            linha = entrada.readline()
            tupla = linha.split(';')
        dupla = []
        dupla.append(variaveis)
        dupla.append(campos)
        tabelas.append(dupla)
        linha = entrada.readline()
    levs_e_tabs = []
    levs_e_tabs.append(levels)
    levs_e_tabs.append(tabelas)
    return levs_e_tabs

def extrair_variaveis(tabelas):
    variaveis = []
    for i in tabelas:
        for j in i[0]:
            if not any(s == j for s in variaveis):
                variaveis.append(j)
    return variaveis

def escolher_variavel(variaveis):
    print('Escolha a variável correspondente\n')
    count = 1
    count_max = len(variaveis)
    maior = 0
    for i in variaveis:
       if len(i) > maior:
           maior = len(i)
    maior = maior + len(str(count_max)) + 3
    for i in variaveis:
        print(str(count) + ' - ' + i, end = '', flush = True)
        n_spaces = (maior + 1) - (len(i) + len(str(count)) + 3)
        if count % 3 != 0:
            for k in range(n_spaces):
                print(' ',end = '')
        else:
            print('\n',end = '')
        count = count + 1
    opt = input('\nOpção escolhida: ')
    return variaveis[int(opt) - 1]

def reescrever_no_arquivo(tabelas,levels,nome_arq):
    saida = open(nome_arq,'w')
    for j in tabelas:
        index = tabelas.index(j)
        for count in range(int(levels[index])-1):
            saida.write(';')
        saida.write('Level;')
        saida.write(levels[index] + '\n')
        for k in j[0]:
            for count in range(int(levels[index])-1):
                saida.write(';')
            saida.write(k + ';')
            index2 = j[0].index(k)
            for l in j[1][index2]:
                saida.write(l + ';')
            saida.write('\n')
        saida.write('\n')
    saida.close()

def Filtrar_Variaveis_Floats(variaveis,tabelas):
    variaveis_floats =[]
    for k in variaveis:
        VariavelInvalida = False
        for i in tabelas:
            if any(s == k for s in i[0]):
                index = i[0].index(k)
                for j in i[1][index]:
                    if not is_float(j):
                        VariavelInvalida = True
        if not VariavelInvalida:
            variaveis_floats.append(k)
    return variaveis_floats

def Filtrar_Variaveis_INTs(variaveis,tabelas):
    variaveis_INTs =[]
    for k in variaveis:
        VariavelInvalida = False
        for i in tabelas:
            if any(s == k for s in i[0]):
                index = i[0].index(k)
                for j in i[1][index]:
                    if not j.isdigit():
                        VariavelInvalida = True
        if not VariavelInvalida:
            variaveis_INTs.append(k)
    return variaveis_INTs

def ver_nome_arq():
        nome_para_DT = open('NomeArq.txt','r')
        nome_arq = nome_para_DT.read()
        nome_para_DT.close()
        os.remove('NomeArq.txt')
        return nome_arq

def menu():
    print('Selecione uma opção:')
    print('1. Calcular média de valores de uma variável')
    print('2. Calcular desvio padrão dos valores de uma variável')
    print('3. Somar número de acertos')
    print('4. Calcular média de acertos')
    print('5. Escrever resultados no arquivo e sair')

def case_1(tabelas):
    variaveis = extrair_variaveis(tabelas)
    variaveis = Filtrar_Variaveis_Floats(variaveis,tabelas)
    variavel = escolher_variavel(variaveis)
    clear()
    resp = input('Desconsiderar quando ACC = 0?\nS - sim\t\tN- não\nResp: ')
    clear()
    resp = resp.upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida')
        resp = input('Desconsiderar quando ACC = 0?\nS - sim\t\tN- não\nResp: ')
        resp = resp.upper()
        clear()
    if resp == 'S':
        tabelas = calc_media(tabelas,variavel,1)
    else:
        tabelas = calc_media(tabelas,variavel,0)
    return tabelas
def case_2(tabelas):
    variaveis = extrair_variaveis(tabelas)
    variaveis = Filtrar_Variaveis_Floats(variaveis,tabelas)
    variavel = escolher_variavel(variaveis)
    clear()
    resp = input('Desconsiderar quando ACC = 0?\nS - sim\t\tN- não\nResp: ')
    clear()
    resp = resp.upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida')
        resp = input('Desconsiderar quando ACC = 0?\nS - sim\t\tN- não\nResp: ')
        resp = resp.upper()
        clear()
    if resp == 'S':
        tabelas = calc_DP(tabelas,variavel,1)
    else:
        tabelas = calc_DP(tabelas,variavel,0)
    return tabelas
def case_3(tabelas):
    tabelas = sum_acertos(ACC,tabelas)
    return tabelas
def case_4(tabelas):
    tabelas = media_acertos(ACC,tabelas)
    return tabelas
def case_default():
    print('Opção inválida')

dict = {1 : case_1, 2 : case_2, 3 : case_3, 4: case_4}

def switch(x,tabelas):
    tabelas = dict[x](tabelas)
    return tabelas

SAIR = 5
ACC = ''

def DT():
    clear()
    print('\t\t\tDataTools\n')
    levs_e_tabs = []
    nome_arq = ver_nome_arq()
    levs_e_tabs = salva_arq_em_ed(nome_arq)
    tabelas = levs_e_tabs.pop()
    levels = levs_e_tabs.pop()
    print('Qual variável corresponde ao ACC?')
    variaveis = extrair_variaveis(tabelas)
    variaveis = Filtrar_Variaveis_INTs(variaveis,tabelas)
    global ACC
    ACC = escolher_variavel(variaveis)
    opt = 0
    clear() 
    while opt != SAIR:
        menu()
        opt = int(input('\nEscolha um opção: '))
        while opt < 1 or opt > SAIR:
            print('Opção inválida!')
            opt = int(input('Escolha um opção válida: '))
        clear()
        if opt >= 1 and opt <= SAIR - 1:
            tabelas = switch(opt,tabelas)
        clear()
    reescrever_no_arquivo(tabelas,levels,nome_arq)

DT()

