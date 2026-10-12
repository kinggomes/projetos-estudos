#Cheque "teste comp" pra ver a versão original e comparar, eliminamos a "pontuação total" por ser desnecessária

#Função responsável pela pontuação no teste, "resposta" é o parâmetro que se refere ao input do usuário que, dependendo se for a, b ou c, retornará a pontuação correta
def atribuir_pontos(resposta):
    if resposta == "a":
        return 20, 0  #comunicativo, estressado
    elif resposta == "b":
        return 0, 20
    elif resposta == "c":
        return 10, 10
    else:
        print("Escolha inválida. Nenhum ponto marcado.")
        return 0, 0


#Lista com todas as perguntas do teste, cada pergunta ocupa um índice (0, 1, 2...)
perguntas = [
    "Você é uma pessoa comunicativa?",
    "Você trabalha bem em grupo?",
    "Você procura se adaptar ao ambiente ao seu redor?",
    "Você motiva sua equipe para que seja bem-sucedida?",
    " Você costuma tomar a iniciativa em projetos?"
]


#Variáveis para acumular os pontos
pontuacao_comunic=0
pontuacao_estress=0

#Mensagens iniciais e coleta de dados pessoais
print("Teste de Competências:")
print("RESPONDA COM AS LETRAS a, b ou c")
nome=input("\nDigite seu nome: ")
idade=input("Digite sua idade: ")


#Esse loop percorrerá e trará todas as perguntas da lista, o "i" serve para marcar o índice da pergunta (para que esteja enumerada, igual na original) enquanto "pergunta" se refere ao valor daquele índice em si, a própria pergunta. Enumerate é justamente para enumerar e "start=1" define que  numeração começará em 1, para que não tenhamos uma pergunta de "número 0", que é o primeiro índice
for i, pergunta in enumerate(perguntas, start=1):
    print(f"N{i}) {pergunta}")
    print('a)Sim \nb)Não \nc)Talvez')

    #Essa variável pegará a resposta do usuário, usamos "lower" para garantir que todas as letras fiquem em minúsculo (caso o usuário responda em maiúsculo)
    resposta = input("Sua resposta: ").lower()

    #Chamamos a função e enviamos a resposta do usuário como parâmetro e, dependendo da resposta, as duas variáveis abaixo receberão os valores retornados pela função e somarão com a pontuação
    comunic, estress = atribuir_pontos(resposta)
    pontuacao_comunic += comunic
    pontuacao_estress += estress


print(f'\nSeu perfil é {pontuacao_comunic}% COMUNICATIVO. \nSão pessoas que se dão muito bem em ambientes colaborativos.')
print(f'\nSeu perfil é {pontuacao_estress}% ESTRESSADO. \nSão pessoas que não se desenvolvem muito em um ambiente de trabalho, e tendem a se estressar mais.')


