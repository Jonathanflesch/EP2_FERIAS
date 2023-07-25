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
