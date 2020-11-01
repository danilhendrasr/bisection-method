from tabulate import tabulate

"y = x^2 - 6x + 8"

equation = "y = pow(x, 2) - 6*x + 8"

a = 3
b = 6
c = (a + b) / 2
error = 0.005

Fa = evaluateEquation(a)
Fb = evaluateEquation(b)
Fc = evaluateEquation(c)

ar = []
tableHeaders = ["Iterasi", "a", "b", "c", "F(a)", "F(b)", "F(c)"]

iterasi = 1
stop = False
while not stop:
    ar.append([iterasi, a, b, c, Fa, Fb, Fc])

    if Fa > 0 and Fc > 0 or Fa < 0 and Fc < 0:
        a = c
    else:
        b = c

    if abs(Fc) <= error:
        hasil = c
        stop = True

    c = (a + b) / 2
    Fa = evaluateEquation(a)
    Fb = evaluateEquation(b)
    Fc = evaluateEquation(c)

    iterasi += 1

print(tabulate(ar, headers=tableHeaders, tablefmt="github"))
print("\n---Hasil---")
print("Iterasi ke-: ", iterasi-1)
print("Aproksimasi akar: ", hasil)


def evaluateEquation(number):
    return eval(equation[4:].replace("x", str(number)))
