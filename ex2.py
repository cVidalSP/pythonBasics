
print('Exercicio 2 - A sequencia | An = ( 1 + 1/n ) ^ n | converge para 2.7182...')

print('|  N  |    f(n)   |')
for x in range(50000):
    aux = x + 1.0
    number = (1.0 + ( 1.0 / aux )) ** aux
    if x < 9 :
        print('|  %d  |  %f  |' %(aux , number))
    else: print('|  %d |  %f  |' %(aux , number))