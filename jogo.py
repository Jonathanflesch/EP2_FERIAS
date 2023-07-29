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

#Funcao 6
def questao_para_texto(dicionario,n):
    titulo = dicionario['titulo']
    opcoes =''
    for opcao in dicionario['opcoes']:
        chance = dicionario['opcoes'][opcao]
        opcoes += f'{opcao}: {chance}\n'

    final =f'''
----------------------------------------
QUESTAO {n}

{titulo}

RESPOSTAS:
{opcoes}'''
    return final

#Ultima funcao
def gera_ajuda(questao):
    erradas=[]
    dicadas=[]
    correta = questao['correta']
    for opcao in questao['opcoes']:
        if opcao != correta:
            erradas.append(opcao)
    escolhida = random.choice(erradas)
    for o in questao['opcoes']:
        if o == escolhida and o not in dicadas:
            dica = questao['opcoes'][o]
            dicadas.append(o)
    
    return f'DICA:\nOpções certamente erradas: {dica}'



quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

faceis =[]
medios=[]
dificeis=[]
for q in quest:
    if q['nivel']=='facil':
        faceis.append(q)
    elif q['nivel']=='medio':
        medios.append(q)
    elif q['nivel']=='dificil':
        dificeis.append(q)
alternativas = ['A','B','C','D']
questoes = transforma_base(quest)
nivel = 'facil'
sorteadas =[]
contador = 1
ajudas=0
pulos=0
premio = 0
print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
print("\033[1;35;40mOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer! \033[1;36;40m")
nome = input('Qual o seu nome? ')
print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
continuar = input('Aperte ENTER para continuar: ')
if continuar =='':
    print('Vamos comecar:\n\n')
    while continuar == '':
        print(f'O seu premio atual é de {premio}')
        if premio >= 1000000:
            break
        questao = sorteia_questao_inedita(questoes,nivel,sorteadas)
        texto = questao_para_texto(questao,contador)
        correta= questao['correta']
        print(texto)
        resposta = input('Resposta: ')
        if resposta == 'ajuda' and ajudas <2:
            print(gera_ajuda(questao))
            ajudas+=1
        elif resposta == correta:
            print('Voce acertou!')
            contador+=1
            if premio >= 500:
                premio *= 2
            else:
                premio = 500
        elif resposta == 'pular' and pulos<3:
            contador+=1
            pulos +=1
            break
        elif resposta == 'parar':
            break
        elif resposta not in alternativas:
            print('Opcao invalida!')
            print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
        else:
            print('Voce errou!')
            print('Volte sempre!')
            break
        continuar = input('Aperte ENTER para a proxima questao ou digite parar para acabar o jogo:\n\n')
print('\n\nBom jogo!')
print('Volte sempre!')
print(f'O seu premio final foi de: {premio}')