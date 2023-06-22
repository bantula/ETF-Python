def unos():
    ''' U ovoj funkciji sam uneo sve podatke koji su mi dati. U svakom ciklusu petlje sam
    prosirio duzinu liste za jos jednu nulu, pa sam dodao novi clan liste. '''

    broj_osoba = int(input())

    opseg_godista = list(input().split("-"))

    lista_ljudi = []

    for i in range(broj_osoba):
        lista_ljudi.append(0)
        nova_osoba = list(input().split(","))
        lista_ljudi[i] = nova_osoba

    return lista_ljudi, opseg_godista


def kategorije(lista_ljudi, opseg_godista):

    '''Ovde racunam BMI svake osobe i dodajem je u njenu kategoriju ako je rodjena u datom
    opsegu godina. Bilo mi je lakse da smestim broj ljudi po kategoriji u listu, nego da pravim
    4 nove promenljive. Takodje sam izbrisao funkciju koja mi racuna BMI, cisto radi pojednostavljivanja. '''

    broj_osoba = len(lista_ljudi)

    resenje_kategorije = [0,0,0,0]

    for i in range(broj_osoba):

        visina = float(lista_ljudi[i][2]) / 100

        tezina = float(lista_ljudi[i][3])

        BMI = round(tezina / visina ** 2, 2)

        godiste = int(lista_ljudi[i][4])
        godina1 = int(opseg_godista[0])
        godina2 = int(opseg_godista[1])

        if (godiste >= godina1) and (godiste <= godina2):

            if BMI < 18.5:
                resenje_kategorije[0] += 1

            elif (BMI >= 18.5) and (BMI < 25):
                resenje_kategorije[1] += 1

            elif (BMI >= 25) and (BMI < 30):
                resenje_kategorije[2] += 1

            elif BMI >= 30:
                resenje_kategorije[3] += 1


    return resenje_kategorije


def ispis(lista_ljudi, resenje_kategorije):

    ''' Ovde proveravam unos koristnika, zato sto ovde kontrolisem sta program treba da ispise.
    Bila mi je neophodna petlja u ovoj funkciji, da bi za svaku osobu ispis bio onakav kako je trazeno. '''

    broj_osoba = len(lista_ljudi)

    if broj_osoba <= 0:
        return None
    else:
        for i in range(broj_osoba):

            visina = float(lista_ljudi[i][2]) / 100

            tezina = float(lista_ljudi[i][3])

            BMI = tezina / visina ** 2

            if (float(lista_ljudi[i][3]) == 0) or (float(lista_ljudi[i][2]) == 0):
                return None
            if (lista_ljudi[i][5] != 'M') and (lista_ljudi[i][5] != 'F'):
                return None

            print(lista_ljudi[i][0], lista_ljudi[i][1], lista_ljudi[i][4], "{:0.2f}".format(BMI))


        print("NEUHRANJENOST: {}".format(resenje_kategorije[0]))
        print("IDEALNA MASA: {}".format(resenje_kategorije[1]))
        print("PREKOMERNA MASA: {}".format(resenje_kategorije[2]))
        print("GOJAZNOST: {}".format(resenje_kategorije[3]))

    return None

''' Ovde krece moj main program. Mislim da jos moze da se pojednostavi, ali se tu gubi preglednost koda. '''

lista_ljudi, opseg_godista = unos()

resenje_kategorije = kategorije(lista_ljudi, opseg_godista)

ispis(lista_ljudi, resenje_kategorije)
