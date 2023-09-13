from scipy.optimize import minimize
import numpy as np

def objective(x):
    return -np.product(x)

def nonlinearconstraint(x):
    return x[0]*x[1] - 3000

def linearconstraint(x):
    return 500 - (x[0] + x[1] + x[2])

def xpositivityconstraint(x):
    return x[0]

def ypositivityconstraint(x):
    return x[1]

def zpositivityconstraint(x):
    return x[2]

if __name__ == '__main__':
    x0 = np.array([100, 100, 1])

    result = minimize(objective, x0, method="COBYLA", constraints=[
        {'type': 'ineq', 'fun': nonlinearconstraint},
        {'type': 'ineq', 'fun': linearconstraint},
        {'type': 'ineq', 'fun': xpositivityconstraint},
        {'type': 'ineq', 'fun': ypositivityconstraint},
        {'type': 'ineq', 'fun': zpositivityconstraint}])

    print(result)
