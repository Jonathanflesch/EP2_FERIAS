import random
#Funcao 1
def transforma_base(lista):
    if len(lista)==0:
        return {}
    faceis=[]
    medio=[]
    dificil=[]
    final = dict()
    for questao in lista:
        if questao['nivel']=='facil':
            faceis.append(questao)
        elif questao['nivel']=='medio':
            medio.append(questao)
        else:
            dificil.append(questao)
    if len(faceis)>0:
        final['facil']=faceis
    if len(medio)>0:
        final['medio']=medio
    if len(dificil)>0:
        final['dificil']=dificil
    return final

#Funcao 2
def valida_questao(dicionario):
    print(dicionario)
    final ={}
    niveis = ['facil','medio','dificil']
    letras=['A','B','C','D']
    chaves = dicionario.keys()
    if 'titulo'not in chaves:
        final['titulo']= 'nao_encontrado'
    if 'nivel' not in chaves:
        final['nivel']= 'nao_encontrado'
    if 'opcoes' not in chaves:
        final['opcoes']= 'nao_encontrado'
    if 'correta' not in chaves:
        final['correta']= 'nao_encontrado'
    if len(dicionario)<4 or len(dicionario)>4:
        final['outro']= 'numero_chaves_invalido'
    if 'titulo' in chaves:
        t = dicionario['titulo'].strip()
        if len(t)==0:
            final['titulo']='vazio'
    if 'nivel' in chaves:
        if dicionario['nivel'] not in niveis:
            final['nivel']='valor_errado'
    if 'opcoes' in chaves:
        if len(dicionario['opcoes'])<4 or len(dicionario['opcoes'])>4:
            final['opcoes']= 'tamanho_invalido'
        else:
            for opcao in dicionario['opcoes']:
                if opcao not in letras:
                    final['opcoes']= 'chave_invalida_ou_nao_encontrada'
                if opcao in letras:
                    x=dicionario['opcoes'][opcao].strip()
                    if len(x)==0:
                        if 'opcoes' not in final:
                            final['opcoes']={}
                        final['opcoes'][opcao]= 'vazia'
    if 'correta' in chaves:
        if dicionario['correta'] not in letras:
            final['correta']= 'valor_errado'
    return final

#Funcao 3

def valida_questoes(lista):
    novo =[]
    for questao in lista:
        problemas = valida_questao(questao)
        novo.append(problemas)
    return novo

#Funcao 4   

import random
def sorteia_questao(dicionario, nivel):
    sorteada = random.choice(dicionario[nivel])
    return sorteada

#Funcao 5

def sorteia_questao_inedita(dicionario,nivel,sorteadas):
    sorte = sorteia_questao(dicionario,nivel)
    while sorte in sorteadas:
        sorte = sorteia_questao(dicionario,nivel)
    sorteadas.append(sorte)
    return sorte