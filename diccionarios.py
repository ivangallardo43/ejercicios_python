def run():
    mi_diccionario = {
        'llave1': 1342,
        'llave2': 29191,
        'llave3': 312,

    } 
    print(mi_diccionario['llave2'])


    for pais in mi_diccionario.keys():
        print(pais)


    for pais in mi_diccionario.values():
        print(pais)


    for pais, poblacion in mi_diccionario.items():
        print(pais + ' tiene ' + str(poblacion) + ' habiatantes ')

if __name__ == '__main__':
    run()

