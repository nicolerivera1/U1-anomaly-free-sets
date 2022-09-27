#!/usr/bin/env python3

r"""
U1 anomaly free sets module
"""

# librerias
import numpy as np
import multiprocessing
import time

# =========================================================
# Funciones
# =========================================================


def merge_op(x, y):

    """
    merge operation for z with specified x, y
    """
    return np.sum(x * (y**2)) * x - np.sum((x**2) * y) * y


def even(n):
    """even sized U1 solution calculator"""

    m = int(n / 2 - 1)  # k, l size

    k = np.random.randint(1, 10, size=m)
    l = np.random.randint(1, 10, size=m)

    # generate plus and minus vector
    vp = np.concatenate(([l[0]], k, [-l[0]], -k))
    vm = np.concatenate(([0, 0], l, -l))

    # calculate z
    z = merge_op(vp, vm)

    return z


def odd(n):
    """odd sized U1 solution calculator"""

    m = int((n - 3) / 2)  # k, l size

    k = np.random.randint(1, 10, size=m + 1)
    l = np.random.randint(1, 10, size=m)

    # generate plus and minus vector
    up = np.concatenate(([0], k, -k))
    um = np.concatenate((l, [k[0], 0], -l, [-k[0]]))

    # calculate z
    z = merge_op(up, um)

    return z


def no_vectorlike(z):
    """classifies if z is vector-like or quiral solution"""

    # gets unique values of z and its absolute value elemets
    uniq_abs = np.unique(np.abs(z)).shape[0]
    uniq_all = np.unique(z).shape[0]

    if uniq_abs == uniq_all:
        # if unique values are equal to absolute unique values the z is quiral
        return 1
    else:
        # otherwise is vector-like
        return 0


def prueba_U1(q):
    """proof operations of U1 group"""

    a3 = np.sum(q**3)
    a1 = np.sum(q)

    return (a3, a1)


# Funcion principal


def joint(n0):
    """main function to calculate quiral U1 solutions"""

    rs = 0  # aceptance variable - 0 is no-quiral, 1 is quiral

    while rs == 0:

        # gets z according to case
        if n0 % 2 == 0 and n0 > 2:
            zf = even(n0)
        elif n0 % 2 != 0 and n0 >= 5:
            zf = odd(n0)
        else:
            print("ingrese entero positivo válido")
            rs = 2
            break

        div = np.gcd.reduce(zf)  # finds z greater common divisor

        rs = no_vectorlike(zf)  # evaluates if z is vector-like

        # evaluates other conditions over z
        if rs == 1:
            zn = zf / div  # reduced z by its gcd
            if np.any(np.abs(zn) > 30) or np.any(np.abs(zn) == 0):
                # all elements must be non zero and minor than 30
                rs = 0
                continue
            else:
                # return (zn, div) #use this if you also need gcd information
                return zn  # use this if you only need z
                break


# --- size of solution --- #
n_values = np.full(10000, 5)

# multiprocessing
if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    start_time = time.perf_counter()
    result = pool.map(joint, n_values)
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")

    for z in np.unique(result, axis=0):
        print(z)
