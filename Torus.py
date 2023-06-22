import math

B0 = 1
H0 = 1000
I = 0.2
a = 0.005
b = 0.01
h = a
N = 1000
fluks = 0.038

br_podeoka = 10000

def prva_fja(c):
    podeoci_prvi = (c - a) / br_podeoka
    prvi_fluks = 0

    for i in range(br_podeoka):
        prvi_fluks += math.atan((N * I) / (2 * math.pi * (i * podeoci_prvi + a) * H0)) * podeoci_prvi

    return 1.1 * prvi_fluks


def druga_fja(c):
    podeoci_drugi = (b - c) / br_podeoka
    drugi_fluks = 0

    for i in range(br_podeoka):
        drugi_fluks += math.atan((50 * N * I) / (2 * math.pi * (i * podeoci_drugi + c) * H0)) * podeoci_drugi

    return drugi_fluks

min = 1000
pravi_fluks = 0
c = 0

probni_fluks = 0

brojac = a

while brojac <= b:
    pravi_fluks = N * B0 * h * (prva_fja(brojac) + druga_fja(brojac))

    if abs(fluks - pravi_fluks) < min:
        c = brojac
        min = abs(fluks - pravi_fluks)
        probni_fluks = pravi_fluks
    brojac += 0.00001

print("Razlika izmedju pravog fluksa i izracunatog:", min)
print("Fluks za granicu c:", probni_fluks)
print("Trazena vrednost za c je:",round(c,5))