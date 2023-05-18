def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    secret_word= "banana"
    letras_corretas=['_',"_","_","_","_","_"]

    enforcou=False
    acertou=False

    #enquanto (True and True):
    while not enforcou and not acertou:
        
        chute= input(f'Chute uma letra => {letras_corretas} :')
        chute= chute.strip()

        index=0
        for letra in secret_word:
            if chute.upper()== letra.upper():
               letras_corretas[index]= letra
            index+=1        
        print(letras_corretas)


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
