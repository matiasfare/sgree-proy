def input_num():
    numerico = False
    num = 0
    while(not numerico):
        try:
            num = input(int())
            numerico = True
        except ValueError:
            print("Error, Ingrese una opcion valida: ")
    return num
