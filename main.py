from tabulate import tabulate

equation = "y = pow(x, 3) - 7*x + 1"

a = 2.5
b = 2.6
c = (a + b) / 2

Fa = eval(equation[4:].replace("x", str(a)))
Fb = eval(equation[4:].replace("x", str(b)))
Fc = eval(equation[4:].replace("x", str(c)))

ar = []
tableHeaders = ["Iterasi", "a", "b", "c", "F(a)", "F(b)", "F(c)"]

iterasi = 1
stop = False
while not stop:
    ar.append([iterasi, a, b, c, Fa, Fb, Fc])

    if iterasi >= 1:
        stop = True

    iterasi += 1

print(tabulate(ar, headers=tableHeaders, tablefmt="github"))
