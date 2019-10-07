#kNN

import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def abs(num):
    if num<0:
        return num*(-1)
    else:
        return num
    

def distancia(v1,v2):
    dim,soma = len(v1), 0
    for i in range(dim-1):# nao quer calcular o ultimo dado(saida)
        soma += math.pow((abs(v1[i] - v2[i])), 2)
    return (math.sqrt(soma))

def classifica(s,treina, k=5):
    dists = {}
    qtde = len(treina)
    for i in range(qtde):
        dist = distancia(s,treina[i])
        dists[i] = dist
        #print(s, '- ', treina[i], '-', dist)
        kVizinhos = sorted(dists, key=dists.get)[:k]#o get traz o valor, colocando em ordem e pegando somente os k primeiros
       
        classe1,classe2 = 0,0
        for p in kVizinhos:
            if(treina[p][-1]==1):
                classe1+= 1
            else:
                classe2+=1
                
        if(classe1 > classe2):
            return 1
        else:
            return 2

inputs =[]
classe=[]
with open('C:/Users/aluno/Desktop/haberman-algorithm-master/haberman.data', 'r') as arq: #abre arquivo, r serve para ler(apenas)
    for linha in arq.readlines(): #le arquiv0
        #print(linha)
        campos = linha.replace('\n', '').split(',') #troca campos em que tem espaco por vazio, separando por ,
        #print(campos)
        inputs.append([int(campos[0]), int(campos[1]),
                      int(campos[2]), int(campos[3])])#para cada campo, converter para inteiro
        classe.append(int(campos[3]))
        
#print(inputs)        
#print(classe)

porcTreina = 0.8 #vai usar 80 por cento dos dados
total = len(inputs)
random.shuffle(inputs)
qtTreina = int(total * porcTreina) #o int faz o numero quebrado virar inteiro
qtTeste = total - qtTreina
#print(total, qtTreina, qtTeste)
treina,teste = [], []
qt = 0
for s in range(total): #qt vai de 0 ao total, pode ser escrito tbm como (0, total)
    if qt < qtTreina:
        treina.append(inputs[qt])
    else:
        teste.append(inputs[qt])
    qt += 1
print(len(inputs), len(treina), len(teste)) # len e o tamanho

acertos = 0
for s in teste:
    classe = classifica(s,treina,11)
    print(s, ' = ', classe)
    if (classe == s[-1]):
        acertos +=1
    
print('Amostras = ', len(teste))
print('Acertos = ', acertos)
print('Precisão = ', (acertos/len(teste))*100)
    
fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')
ax.set_xlabel('Idade')
ax.set_ylabel('Ano')
ax.set_zlabel('Nódulos')

for s in teste:
    if(s[-1]==1):
        ax.scatter(s[0],s[1],s[2],c='b', marker='s')
    else:
        ax.scatter(s[0],s[1],s[2],c='r', marker='o')
    
fig.show()


       #dist = distancia(treina[0], treina[1])
#print(dist)


