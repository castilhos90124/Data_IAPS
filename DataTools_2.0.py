import os

error = True
choice = 0

while error:

    error = False

    print("Que tipo de arquivo sera inserido ?")
    print("1: Os do Pedro")
    print("2: IAPS / Attractfaces")

    choice = input()
    
    if choice == "1":
        import parte1
        import parte2


    elif choice == "2":
        import Main

    else:
        error = True
        os.system("CLS")
        print("Opcao invalida !")
