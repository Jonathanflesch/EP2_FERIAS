#Codigo 1
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

#Codigo 2

def valida_questao(questao):
    validacao = {}
    chaves = ["titulo", "nivel", "opcoes", "correta"]
    chaves_opcoes = ['A', 'B', 'C', 'D']
    
    for chave in chaves:
        if chave not in questao:
            validacao[chave] = 'nao_encontrado'

    if len(questao) != len(chaves):
        validacao['outro'] = 'numero_chaves_invalido'

    if 'nivel' in questao and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        validacao['nivel'] = 'valor_errado'
    
    if 'opcoes' in questao and len(questao['opcoes']) != 4:
        validacao['opcoes'] = 'tamanho_invalido'

    if 'opcoes' in questao and len(questao['opcoes']) == 4 and 'opcoes' not in validacao:
        opcoes_vazias = {}

    return validacao