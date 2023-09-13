from scipy.optimize import linprog
import numpy as np


if __name__ == '__main__':

    c = np.array([-3, 1, -11])

    A = np.array([[-1, 1, -7], [3, -1, 2], [2, 0, 4], [2, -4, 1]])

    b = np.array([13, 0, 3, 3])


    highs_ds_result = linprog(c, A_ub=A, b_ub=b, method='highs-ds')

    print(f'Usando el método highs-ds: \n \n {highs_ds_result} \n \n')

    highs_ipm_result = linprog(c, A_ub=A, b_ub=b, method='highs-ipm')

    print(f'Usando el método highs-ipm: \n \n {highs_ipm_result} \n \n')


