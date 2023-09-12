import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from sympy import symbols, Eq, solve

def system(x):
    return [
        (x[0] - 4)**2 + 3*x[1]**2 - 20,
        x[0] + 8*(x[1] + 1)**2 - 10
    ]

if __name__=='__main__':

    scipy_solution = fsolve(system, [0, 0])
    print('scipy_solution:', scipy_solution)

    x, y = symbols('x y')
    eq1 = Eq((x - 4)**2 + 3*y**2 - 20, 0)
    eq2 = Eq(x + 8*(y + 1)**2 - 10, 0)
    sympy_solution = solve([eq1, eq2], [x, y], dict=True)

    first_sympy_solution_values = [sp.re(sympy_solution[0][x].evalf()), sp.re(sympy_solution[0][y].evalf())]
    second_sympy_solution_values = [sp.re(sympy_solution[1][x].evalf()), sp.re(sympy_solution[1][y].evalf())]
    print('First sympy_solution:', first_sympy_solution_values)
    print('Second sympy_solution:', second_sympy_solution_values)

    x = np.linspace(-2, 11, 1000)
    y = np.linspace(-4, 4, 1000)

    X, Y = np.meshgrid(x, y)
    F = (X - 4)**2 + 3*Y**2 - 20
    G = X + 8*(Y + 1)**2 - 10

    plt.contour(X, Y, F, [0], colors='red')
    plt.contour(X, Y, G, [0], colors='blue')
    plt.plot(scipy_solution[0], scipy_solution[1], 'o', color='black')
    plt.plot(first_sympy_solution_values[0], first_sympy_solution_values[1], 'o', color='green')
    plt.plot(second_sympy_solution_values[0], second_sympy_solution_values[1], 'o', color='green')
    plt.show()

