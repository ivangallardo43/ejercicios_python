#numerox = int(input('esccriba el numero : '))
#contador = 1
#potencia = int(input('esccriba la potencia: '))
#hasta = int(input('hasta donde'))
#if potencia > 1:

#resultado = numerox**potencia
#print(resultado)


def run():
    potencia = int(input('Que potencia deseas conocer: '))
    numerox = int(input(' Hasta que numero la deseas : '))
    contador = 0

    if potencia == 0:
        print('No es posible la potencia de 0 ')
    else:
        potencia_2 = potencia**contador

        while potencia_2 == numerox:
            print(str(potencia) + ' elevado a ' + str(contador) + ' es igual a =  ' + str(potencia_2))
            contador = contador + 1
            potencia_2 = potencia **contador


if __name__ == '__main__':
    run()