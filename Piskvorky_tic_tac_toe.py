# Project2_Ondrej Knopp


def vygeneruj_matici(nradku, nsloupcu):
    matrix = [[0] * nsloupcu for i in range(nradku)]
    return matrix


def vykresli_matici(matice):
    for radek in matice:
        text = ""
        for symbol in radek:
            if symbol == 0:
                text += " |"
            elif symbol == 1:
                text += "o|"
            elif symbol == 2:
                text += "x|"
            else:
                text = "?|"
        print(text[:-1])
        # radek = "-"*len(matice[0])*2
        # print(radek[:-1])


def vitezstvi_radku(matice, hrac):
    for radek in matice:
        vitezstvi = True
        for symbol in radek:
            if symbol != hrac:
                vitezstvi = False
        if vitezstvi:
            return True
    return False


def vitezstvi_sloupcu(matice, hrac):
    nradku = len(matice)
    nsloupcu = len(matice[0])
    for jsloupec in range(nsloupcu):
        vitezstvi = True
        for iradek in range(nradku):
            if matice[iradek][jsloupec] != hrac:
                vitezstvi = False
        if vitezstvi:
            return True
    return False


def vitezstvi_diagonala_levoprava(matice, hrac):
    # staci jeden index [0][0],[1][1],[2][2],[2][0],[1][1],[0][2] - jeden cyklus pro diagon jedním směrem, druhý cyklus pro diagonálu druhým směrem
    #pass  # zatim
    rozmer = len(matice[0])
    vitezstvi = True
    for i in range(rozmer):
        if matice[i][i] != hrac:
            vitezstvi = False

    if vitezstvi:
            return True

    return False

def vitezstvi_diagonala_pravoleva(matice, hrac):
    # staci jeden index [0][0],[1][1],[2][2],[2][0],[1][1],[0][2] - jeden cyklus pro diagon jedním směrem, druhý cyklus pro diagonálu druhým směrem
    #pass  # zatim
    rozmer = len(matice[0])
    vitezstvi = True
    for i in range(rozmer):
        if matice[i][(rozmer-1)-i] != hrac:
            vitezstvi = False

    if vitezstvi:
            return True

    return False



def preved_na_pozici(cislo, nsloupcu):
    cislo = cislo - 1
    radek = cislo // nsloupcu
    sloupec = cislo % nsloupcu

    return (radek, sloupec)


def main():
    rozmer = int(input("Zadej rozměr hrací plochy (bude vygenerována čtvercová matice): "))
    print("Skvělé, nyní budeš postupně vyzýván k zadání pole, které chceš obsadit v rozsahu 1 až",rozmer**2,".")
    piskvorky = vygeneruj_matici(rozmer, rozmer)
    game_on = True
    tah = 1
    while game_on:
        cislo_hrace = 2 if tah % 2 == 0 else 1
        print("Hráči číslo " + str(cislo_hrace) + ", zadej pozici:")
        cislo = int(input(""))
        # kdyz na pozici uz není O, nemuzu sem uz zapisovat! osetrit
        radek, sloupec = preved_na_pozici(cislo, rozmer)
        if piskvorky[radek][sloupec] == 0:

            symbol = 2 if tah % 2 == 0 else 1
            piskvorky[radek][sloupec] = symbol
            vykresli_matici(piskvorky)
        else:
            print("Tato pozice je už obsazená, zkus jinou..")
            continue

        if vitezstvi_sloupcu(piskvorky, symbol) or vitezstvi_radku(piskvorky, symbol) or vitezstvi_diagonala_levoprava(piskvorky, symbol) or vitezstvi_diagonala_pravoleva(piskvorky, symbol):
            vitezny_znak = "koleček" if symbol == 1 else "křížků"
            print("Vítězství pro hráče", symbol, "se symbolem",vitezny_znak,"!")
            game_on = False
        elif tah >= rozmer**2:
            print("To je game over - remíza, již nejsou volná další pole!")
            game_on = False

        tah = tah + 1





if __name__ == "__main__":
    main()
