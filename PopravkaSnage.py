import numpy as np
import matplotlib.pyplot as plt
import math

E = 1
R1 = 50
R2 = 100
L1 = (25/math.pi)*pow(10, -9)
C1= 1.59*pow(10, -12)

f = np.linspace(0.5, 1.5, 200)*pow(10,9)

omega=2*math.pi*f

'''a=R2*omega*C1
brojilac = E**2*R2
sabirak1 = R1 + R2/(1+a**2)
sabirak2 = omega*L1-R2*a/(1+a)
razdelnik=1/(1+a**2)**2+(a/(1+a))**2'''

xc = 1/(omega*C1)
xl = omega*L1

brojilac = E**2 * (R2*(xc**2))/(R2**2 + xc**2)
sabirak1 = (R2*(xc**2))/(R2**2 + xc**2) + R1
sabirak2 = xl - ((R2**2)*xc)/(R2**2 + xc**2)

C2 = 1.5*pow(10,-12)
L2 = 5.6*pow(10,-9)
R_2 = 75

xc_ = 1/(omega*C2)
xl_ = omega*L2

brojilac_ = E**2 * (R_2*(xc_**2))/(R_2**2 + xc_**2)
sabirak1_= (R_2*(xc_**2))/(R_2**2 + xc_**2) + R1
sabirak2_ = xl_ - ((R_2**2)*xc_)/(R_2**2 + xc_**2)

Pr1 = brojilac/(sabirak1**2 + sabirak2**2)
Pr2 = brojilac_/(sabirak1_**2 + sabirak2_**2)
y = np.array(Pr1, dtype='float')
z = np.array(Pr2, dtype='float')

fig, ax = plt.subplots()
ax.plot(f, Pr1)
ax.plot(f, Pr2)

ax.set(xlabel='f[GHz]', ylabel='Pr1[W]',
       title='Zavisnost Pr1(f)')

plt.show()

