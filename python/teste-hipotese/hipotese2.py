#Essa é uma versão alternativa do código "hipótese"

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind #Importa a função ttest_ind da biblioteca scipy.stats para comparar duas amostras.

#Geração de dados e do histograma

tamanho_populacao=10000 #Define uma variável para representar o tamanho da população
np.random.seed(2000)    #Define a seed do gerador de números aleatórios, onde os valores serão os mesmos em cada execução
lista_dados=[]

#Por 2 vezes, criam-se dados aleatórios de distribuição normal, que seguirão os parâmetros de média=100 e desvio padrão=10, que serão colocados na variável valor e depois colocadas na lista "lista_dados". Em cada loop, o dado atual do loop é usado para criar 2 histogramas diferentes. Porém, isso acaba gerando 4 histogramas (2 por loop) o que é meio desnecessário. Cada valor de dados também vai para a lista no final do loop
for i in range(2):
    dados=np.random.normal(loc=100, scale=10, size=tamanho_populacao)
    plt.hist(dados) #Cria um primeiro histograma baseado nos pridados
    plt.xlabel("Categorias")  #Rótulo do primeiro eixo x
    plt.ylabel("Quantidade")  #Rótulo do primeiro eixo y
    plt.title('Histograma da Primeira Amostra') # Define o título do primeiro gráfico

    #Cria um segundo histograma, mais especializado para se diferenciar do primeiro
    plt.hist(x=dados, bins='auto', color='#0805aa', alpha=0.7, rwidth=0.85, density=True)
    plt.grid(axis='y', alpha=0.80) # Adiciona uma grade horizontal no eixo y para facilitar a visualização dos dados. 
    plt.xlabel('Categorias') # Define o rótulo do segundo eixo x
    plt.ylabel('Quantidades') # Define o rótulo do segundo eixo x
    plt.title('Histograma da Segunda Amostra') # Define o título do segundo gráfico
    lista_dados.append(dados)
    


plt.show()


#Teste de hipóteses

dados1 = lista_dados[0] #Pega a primeira lista de dados. 
dados2 = lista_dados[1] #Pega a segunda lista de dados. 

#Essa função calcula a diferença estatística entre as médias de dados1 (o primeiro conjunto de dados gravados na lista, pelo primeiro loop) e de dados2 (segundo conjunto, resultado do segundo loop). Esse valor estatístico vai para a variável "estatistica" e o p-valor, que também é calculado ainda nessa mesma função, vai para a variável "p_valor". Essa função só pode ser usada uma vez com esses parâmetros, por isso a atribuição não pode ser separada.
estatistica, p_valor = ttest_ind(dados1, dados2) 

#Imprime os valores da estatística do teste e do p-valor, formatados com três casas decimais. 
print(f"Estatística: {estatistica: .3f}  P-Valor: {p_valor: .3f}")


#Baseaso no valor de p-valor, esse if irá decidir se a hipótese nula (hipótese onde a diferença entre as médias é pouca ou semelhante) deve ser aceita ou não. Se for alto, ela é aceita, se não ela é rejeitada.
if p_valor>0.05:
    print("Aceita H0")
else:
    print("Rejeita H0")
