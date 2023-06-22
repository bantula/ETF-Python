import math

a = 0.1
I = 1
x2 = (2*a)/(math.sqrt(3))
mi0 = 4 * math.pi * 1e-7
br_podeoka = 10000
B2 = 0

const = (mi0 * I) / (4 * math.pi)

def funkcijaB2(ugao, desna_strana):
    if desna_strana == False:
        return 1 / ((a / math.sqrt(3)) * (2 * math.cos(ugao) + math.sqrt(4 * (math.cos(ugao)) ** 2 - 1)))
    else:
        return 1 / ((a / math.sqrt(3)) * (2 * math.cos(ugao) - math.sqrt(4 * (math.cos(ugao)) ** 2 - 1)))

def funkcijaB1(x1, ugao):
    return 1 / (x1 * math.cos(math.pi - ugao) + math.sqrt((x1 * math.cos(math.pi - ugao)) ** 2 - x1 ** 2 + a ** 2))

podeoci_dva = (math.pi / 3) / br_podeoka
podeoci_jedan = math.pi / br_podeoka

for i in range(br_podeoka):
    B2 = B2 + 2 * const * podeoci_dva * abs(funkcijaB2(i * podeoci_dva, True) - funkcijaB2(i * podeoci_dva, False))

print(B2)

min = 10000
razlika = 0
x1 = 0
duzina = 0

for duzina in range(0, int(a * br_podeoka)):
    duzina = duzina/br_podeoka
    B1 = 0

    for ugao in range(br_podeoka):
        B1 = B1 + 2 * const * podeoci_jedan * funkcijaB1(duzina, ugao * podeoci_jedan)

    razlika = abs(B2-B1)
    if razlika <= min:
        min = razlika
        x1 = duzina


print("Trazeno rastojanje x1 je {:0.3f} metara".format(x1))

