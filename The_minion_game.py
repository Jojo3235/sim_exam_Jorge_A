VOCALES = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
SI = ['S', 's', 'Y', 'y', 'Si', 'si', 'SI', 'sI', 'Yes', 'yes', 'YES', 'yES', 'yEs', 'YeS', 'yeS']
NO = ['N', 'n', 'No', 'no', 'NO', 'nO']

def input_string():
    string = input("Introduce una sucesión de vocales y consonantes: ")
    try:
       string = str(string)
    except ValueError:
        print("Error: No se ha introducido una letra o combinación de estas.") 
    return string

def minion_game(string):
    longitud = len(string)
    Kevin = 0
    Stuart = 0

    for i in range(longitud):
        if string[i] in VOCALES:
            Kevin += (longitud - i)
        else:
            Stuart += (longitud - i)

    if Kevin > Stuart:
        print('Kevin', Kevin)
    elif Kevin < Stuart:
        print('Stuart', Stuart)
    else:
        print('Draw')

def jugar_de_nuevo():
    respuesta = input("¿Quieres jugar de nuevo? (S/N): ")
    try:
        respuesta = str(respuesta)
    except ValueError:
        print("Error: No se ha introducido una letra o combinación de estas.")
    if respuesta in SI:
        return True
    elif respuesta in NO:
        return False
    else:
        print("Error: No se ha introducido una letra o combinación de estas.")
        return False

def main():
    jugar = True
    while jugar == True:
        s = input_string()
        minion_game(s)
        jugar = jugar_de_nuevo()

if __name__ == '__main__':
    main()