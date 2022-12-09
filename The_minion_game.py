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
        if string[i] in 'AEIOU':
            Kevin += longitud - i
        else:
            Stuart += longitud - i

    if Kevin > Stuart:
        print('Kevin', Kevin)
    elif Kevin < Stuart:
        print('Stuart', Stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input_string()
    minion_game(s)