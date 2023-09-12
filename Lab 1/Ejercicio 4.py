from scipy.optimize import minimize
import numpy as np

def objective(x):
    return -np.product(x)

def nonlinearconstraint(x):
    return x[0]*x[1] - 3000

def linearconstraint(x):
    return 500 - (x[0] + x[1] + x[2])

if __name__ == '__main__':
    x0 = np.array([100, 100, 1])

    result = minimize(objective, x0, method='SLSQP', constraints=[{'type': 'ineq', 'fun': nonlinearconstraint}, {'type': 'ineq', 'fun': linearconstraint}])

    print(result)
