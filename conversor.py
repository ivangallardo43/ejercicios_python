menu = """
Bienvenido al conversor 💰🤑

1 - pesos de colombia
2 - pesos de argentina
3 - pesos estandar

Eliga una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cunato tienes 1 : ")
    pesos = float(pesos)
    valor_dolar = 3911
    dolares = pesos / valor_dolar
    dolares = round(dolares, 5)
    dolares = str(dolares)
    print("tienes $ " + dolares + " dólares ")

elif opcion == 2:
    pesos = input("Cunato tienes 2 : ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 5)
    dolares = str(dolares)
    print("tienes $ " + dolares + " dólares ")
elif opcion == 3:
    pesos = input("Cunato tienes 3 : ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 5)
    dolares = str(dolares)
    print("tienes $ " + dolares + " dólares ")
else:
    print('ingresa algo bien por favor')


