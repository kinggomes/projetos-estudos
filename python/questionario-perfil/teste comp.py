pontuacao_comunic=0
pontuacao_estress=0
pontuacao=0

print('Teste de Competências:')
print('RESPONDA COM AS LETRAS "a,b,ou c"')
nome=input('\nDigite seu nome:')
idade=input('Digite sua idade:')

print('\nN1) Você é uma pessoa comunicativa?')
print('a)Sim  \nb)Não  \nc)Talvez')
resp1=input('Sua resposta:')
if resp1=='a':
    pontuacao_comunic+=20
    pontuacao+=20
elif resp1=='b':
    pontuacao_estress+=20
    pontuacao+=20
elif resp1=='c':
    pontuacao_estress+=10
    pontuacao_comunic+=10
    pontuacao+=10

print('\nN2) Você trabalha bem em grupo?')
print('a)Sim \nb)Não \nc)Talvez')
resp2=input('Sua resposta:')
if resp2=='a':
    pontuacao_comunic+=20
    pontuacao+=20
elif resp2=='b':
    pontuacao_estress+=20
    pontuacao+=20
elif resp2=='c':
    pontuacao_estress+=10
    pontuacao_comunic+=10
    pontuacao+=10

print('\nN3) Você procura se adaptar ao ambiente ao seu redor?')
print('a)Sim \nb)Não \nc)Talvez')
resp3=input('Sua resposta:')
if resp3=='a':
    pontuacao_comunic+=20
    pontuacao+=20
elif resp3=='b':
    pontuacao_estress+=20
    pontuacao+=20
elif resp3=='c':
    pontuacao_estress+=10
    pontuacao_comunic+=10
    pontuacao+=10

print('\nN4) Você motiva sua equipe para que seja bem-sucedida?')
print('a)Sim \nb)Não \nc)Talvez')
resp4=input('Sua resposta:')
if resp4=='a':
    pontuacao_comunic+=20
    pontuacao+=20
elif resp4=='b':
    pontuacao_estress+=20
    pontuacao+=20
elif resp4=='c':
    pontuacao_estress+=10
    pontuacao_comunic+=10
    pontuacao+=10

print('\nN5) Você costuma tomar a iniciativa em projetos?')
print('a)Sim \nb)Não \nc)Talvez')
resp5=input('Sua resposta:')
if resp5=='a':
    pontuacao_comunic+=20
    pontuacao+=20
elif resp5=='b':
    pontuacao_estress+=20
    pontuacao+=20
elif resp5=='c':
    pontuacao_estress+=10
    pontuacao_comunic+=10
    pontuacao+=10


pontuacao_comunic=pontuacao_comunic/1
pontuacao_estress=pontuacao_estress/1       
print(f'\nSeu perfil é {pontuacao_comunic}% COMUNICATIVO. \nSão pessoas que se dão muito bem em ambientes colaborativos.')
print(f'\nSeu perfil é {pontuacao_estress}% ESTRESSADO. \nSão pessoas que não se desenvolvem muito em um ambiente de trabalho, e tendem a se estressar mais.')



