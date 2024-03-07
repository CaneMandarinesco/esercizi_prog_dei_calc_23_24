# determinare date due stinghe x e y, se x precede y
# esempio di ordinamento delle stiringhe:
# ciao < barbabietola < barbabietolu < barbabietolecotte
# barbapapa < papabarba
# a differenza del programma del Rossi, da qui non sono ingrado
# di capire se 2 stringhe sono uguali, si puo' implementare scrivendo una funzione separata

def x_precede_y(x,y):
    len_x, len_y = len(x), len(y)
    n = 0 # contiene il numero di caratteri piu grade tra x e y

    # compara tutti i caratteri
    if len_x == len_y:
        n = len_x-1 # oppure len_y, tanto e' uguale.
                    # -1 perche' senno' vado fuori dall'array
        i = 0
        while i <= n:
            if x[i] == y[i]:
                i += 1
            elif x[i] < y[i]:
                return True
            else:
                return False

    # se sono arrivato qua vuol dire che posso decidere in base alla 
    # lunghezza delle stringhe
    if len_x < len_y:
        return True
    # else:
    return False

def x_precede_y_output(x,y):
    n = x_precede_y(x,y)
    if n:
        print(x, " precede ", y)
    else: 
        print(y, " precede " , x)
    

def test():
    x_precede_y_output("ciao", "barbabietola")
    x_precede_y_output("barbabietolu", "barbabietola")
    x_precede_y_output("barbabietolu", "barbabietolecotte")
    x_precede_y_output("barbapapa", "papabarba")

m = input("vuoi eseguire un test del programma? (Y/n)")
if m in ["", "Y"]:
    test()

x, y = input("\nstringa 1: "), input("stringa 2: ")
risultato = x_precede_y(x,y)
if risultato:
    print(x, " precede ", y)
else:
    print(y, " precede ", x)