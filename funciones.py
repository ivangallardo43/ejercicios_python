def conversacion(mensaje):
    nombre = input('Dime tu nombre')
    print('Bienvenido ')
    print(nombre)
    print(mensaje)
    print('esta es el curo de aprendizaje')
    print('venceremos')

opcion = int(input('elije una opción (1, 2, 3): '))
if opcion == 1:
    conversacion('elegiste la opcion 1')
elif opcion == 2:
    conversacion('elegiste la 2 ')
elif opcion == 3:
    conversacion('elegiste la opci 3')
else:
    print('elegiste mal, Adios!!!!!!! ')
