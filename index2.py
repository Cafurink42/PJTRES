from random import * 

typeAnumber = int(input('Digite um número de 0 a 1:'))

randomNum = round(random())

if (typeAnumber == randomNum):
    print ('Você deu sorte')
else:
    print ('Você deu azar')
