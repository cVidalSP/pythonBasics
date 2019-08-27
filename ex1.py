print('Exercicio 1 - A sequencia An = 1/n converge para 0. ')
print('Insira um numero de testes: ')
controller = input()
print( '|  N  |     An     |' )
for x in range(controller):
    number = 1.0/(x+1.0)
    if x < 9:
        print( '|  %d  |  %f  |' %(x+1, number) )
    else:
        print( '|  %d |  %f  |' %(x+1, number) )


