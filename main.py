from tabulate import tabulate


def evaluateEquation(number):
    return eval(equation[4:].replace("x", str(number)))


equation = "y = pow(x, 3) - 7*x + 1"

a = 2.5
b = 2.6
c = (a + b) / 2
error = 0.005

Fa = evaluateEquation(a)
Fb = evaluateEquation(b)
Fc = evaluateEquation(c)

ar = []
tableHeaders = ["Iterasi", "a", "b", "c", "F(a)", "F(b)", "F(c)"]

iterasi = 1
stop = False

if Fa * Fb > 0:
    print('Tidak ada akar')
else:
    while not stop:
        ar.append([iterasi, a, b, c, Fa, Fb, Fc])

        if Fa * Fc >= 0:
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
