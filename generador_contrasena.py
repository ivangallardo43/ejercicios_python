import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E']
    minusculas = ['a', 'b', 'c', 'd', 'e']
    simbolos = ['!', '¡', '$', '(', ')']
    numeros = ['1', '2', '3', '4', '5']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(7):
        caracteres_random = random.choice(caracteres)
        contrasena.append(caracteres_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print (' Tu nuevaa contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()