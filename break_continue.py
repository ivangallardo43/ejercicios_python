def run():
    for contador in range(5):
        if contador % 2 != 0:
            continue 
        print(contador)


    for i in range (9,21):
        print(i)
        if i == 17:
            break


    texto = input('escribe : ')
    for letra in texto:
        if letra == 'o' or letra == 'O':
            break
        print(letra)

if __name__ == '__main__':
    run()
