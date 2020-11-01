import os
from tabulate import tabulate


def evaluateEquation(number):
    return eval(equation.replace("x", str(number)))


equationTemplate = "y = x^q - r*x + s"
equation = "pow(x, q) - r*x + s"

print("-- Masukkan persamaan --")
print("Format persamaan:\n ", equationTemplate)
q = int(input("Masukkan nilai q: "))
r = int(input("Masukkan nilai r: "))
s = int(input("Masukkan nilai s: "))

rawEquation = equationTemplate.replace(
    "q", str(q)).replace("r", str(r)).replace("s", str(s))

os.system('cls' if os.name == 'nt' else 'clear')
print("Persamaan yang didapat: ", rawEquation)

print("---------------")
print("Masukkan nilai")
a = float(input("Masukkan nilai selang a: "))
b = float(input("Masukkan nilai selang b: "))
toleransiError = float(input("Masukkan toleransi error: "))

Fa = evaluateEquation(a)
Fb = evaluateEquation(b)

if Fa * Fb > 0:
    print("\n-- Tidak dapat dilakukan operasi... Persamaan tidak memiliki akar --")
    exit()

c = (a + b) / 2
err = abs(b-a)

Fc = evaluateEquation(c)

ar = []
tableHeaders = ["Iterasi", "a", "b", "c", "F(a)", "F(b)", "F(c)", "Error"]

iterasi = 1
stop = False
while not stop:
    ar.append([iterasi, a, b, c, Fa, Fb, Fc, err])

    if Fa * Fc >= 0:
        a = c
    else:
        b = c

    if err <= toleransiError:
        hasil = c
        stop = True

    c = (a + b) / 2
    err = abs(b-a)
    Fa = evaluateEquation(a)
    Fb = evaluateEquation(b)
    Fc = evaluateEquation(c)

    iterasi += 1

print(tabulate(ar, headers=tableHeaders, tablefmt="github"))
print("\n---Hasil---")
print("Iterasi ke-: ", iterasi-1)
print("Aproksimasi akar: ", hasil)
