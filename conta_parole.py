# determinare il numero di parole in una stringa

def conta_parole(a):
    in_parola = a[0] not in ",.; "
    parole = 1 if in_parola else 0

    for n in a:
        if n in ",.; ":
            if in_parola: 
                in_parola = False
        elif not in_parola:
            in_parola = True
            parole += 1
    
    return parole

def test():
    m1 = "When it is angered, ,it immediately.. discharges   the energy stored in the pouches in its cheeks."
    print("\"", m1, "\" ha: ", conta_parole(m1), " parole.\n\n")
    m2 = "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks."
    print("\"", m2, "\" ha: ", conta_parole(m2), " parole.\n\n")
    m3 = "It is waiting for the moment to evolve. At this stage, it can only harden, so it remains motionless to avoid attack."
    print("\"", m3, "\" ha: ", conta_parole(m3), " parole.\n\n")
    m4 = " "
    print("\" \" ha: ", conta_parole(m4), " parole.\n\n")

m = input("vuoi eseguire un test del programma? (Y/n)")
if m in "Y ":
    test()

a = input("scrivi la frase: ")
print("la frase contiene: ", conta_parole(a), " parole.")