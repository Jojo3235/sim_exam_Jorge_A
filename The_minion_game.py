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
    s = input("Introduce una subcadena de la palabra 'BANANA': ")
    minion_game(s)