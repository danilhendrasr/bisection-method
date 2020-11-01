import os
from tabulate import tabulate


def evaluateEquation(number):
    return eval(equation.replace("x", str(number)))


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def exitProgram():
    print("\n-- Tidak dapat dilakukan operasi... Persamaan tidak memiliki akar --")
    exit()


equationTemplate = "y = x^q - r*x + s"
equation = "pow(x, q) - r*x + s"

print("------ Masukkan persamaan ------")
print("\nFormat persamaan:\n ", equationTemplate, "\n")
q = int(input("Masukkan nilai q: "))
r = int(input("Masukkan nilai r: "))
s = int(input("Masukkan nilai s: "))

rawEquation = equationTemplate.replace(
    "q", str(q)).replace("r", str(r)).replace("s", str(s))

clearTerminal()
print("Persamaan yang didapat: ", rawEquation)

print("-----------------------")
a = float(input("Masukkan nilai selang a: "))
b = float(input("Masukkan nilai selang b: "))
toleransiError = float(input("Masukkan nilai toleransi error: "))

Fa = evaluateEquation(a)
Fb = evaluateEquation(b)

if Fa * Fb > 0:
    exitProgram()

c = (a + b) / 2
err = abs(b-a)

Fc = evaluateEquation(c)

ar = []
tableHeaders = ["Iterasi ke-", "a", "b", "c", "F(a)", "F(b)", "F(c)", "Error"]

iterasi = 0
stop = False
while not stop:
    ar.append([iterasi+1, a, b, c, Fa, Fb, Fc, err])

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

clearTerminal()
print(tabulate(ar, headers=tableHeaders, tablefmt="psql"))
print("\n----- Hasil -----")
print("Iterasi ke-{}".format(iterasi))
print("Aproksimasi akar: ", hasil)
