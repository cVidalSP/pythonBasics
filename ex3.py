import math
print(' Exercicio 3 - Encontre os pontos de convergencia para: | An = log(n)/n - Bn = (n)^(1/n) - Cn = sen(n)/n |')

for x in range(10):
    aux = x + 1
    numberA = math.log(aux)/aux
    numberB = aux**(1/aux)
    numberC = math.sin(aux)/aux
    print('| %f | %f | %f |' %( numberA, numberB, numberC ))
