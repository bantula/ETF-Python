def unos_izdavaca():
    return input().strip()

def ucitavanje_datoteke():
    with open('manga.txt', encoding="utf8") as mange:
        i = 0
        matrica_mangi = []

        for line in mange:
            matrica_mangi.append(0)
            matrica_mangi[i] = list(line.split(','))

            for j in range(len(matrica_mangi[i])):
                matrica_mangi[i][j] = matrica_mangi[i][j].strip()
            i += 1
    mange.close()
    return matrica_mangi


def pravljenje_izdavacke_datoteke(matrica_mangi, izdavac):
    fajl_izdavaca = open((izdavac.replace(" ","_")).lower() + '.txt','a')
    mange_izdavaca = []

    for i in range(len(matrica_mangi)):
        matrica_mangi[i][2] = int(matrica_mangi[i][2][0:2]) + 12 * int(matrica_mangi[i][2][3:-1])

        if matrica_mangi[i][1] == izdavac:
            mange_izdavaca.append(matrica_mangi[i][0])

    mange_izdavaca = list(set(mange_izdavaca))
    mange_izdavaca_sortirane = sorted(mange_izdavaca)
    if len(mange_izdavaca_sortirane) == 0:
        fajl_izdavaca.close()
        return None
    matrica_mangi_sortirana = sorted(sorted(matrica_mangi, key=lambda x: x[2]), key=lambda x: x[0])

    for naziv_mange in mange_izdavaca_sortirane:
        broj_tomova = 0
        ukupan_broj_poglavlja = 0
        prosecna_duzina_poglavlja = 0
        ukupna_duzina_poglavlja = 0
        drugi_red = []

        for i in range(len(matrica_mangi_sortirana)):
            if (matrica_mangi_sortirana[i][1] != izdavac) or (naziv_mange != matrica_mangi_sortirana[i][0]):
                continue

            broj_tomova +=1
            ukupan_broj_poglavlja += len(matrica_mangi_sortirana[i]) - 4

            ukupna_duzina_poglavlja += int(matrica_mangi_sortirana[i][3]) - int(matrica_mangi_sortirana[i][4])

            for j in range(4,len(matrica_mangi_sortirana[i])-1):
                drugi_red.append(int(matrica_mangi_sortirana[i][j+1]) - int(matrica_mangi_sortirana[i][j]))

            drugi_red.append(int(matrica_mangi_sortirana[i][3]) - int(matrica_mangi_sortirana[i][-1]))

        prosecna_duzina_poglavlja = float(ukupna_duzina_poglavlja / ukupan_broj_poglavlja)
        prosecna_duzina_poglavlja = '{0:.{1}f}'.format(prosecna_duzina_poglavlja, 2)

        fajl_izdavaca.write(naziv_mange + ', ' + str(broj_tomova) + ', ' + str(ukupan_broj_poglavlja)\
        + ', ' + str(prosecna_duzina_poglavlja) + '\n')
        for k in range(len(drugi_red)-1):
            fajl_izdavaca.write(str(drugi_red[k]) + ', ')
        fajl_izdavaca.write(str(drugi_red[-1]) + '\n')

    fajl_izdavaca.close()
    return None


try:
    izdavac = unos_izdavaca()
    matrica_mangi = ucitavanje_datoteke()
    pravljenje_izdavacke_datoteke(matrica_mangi, izdavac)
except FileNotFoundError:
    print("DAT_GRESKA",end='')
