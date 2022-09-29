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


def even(n, m_max=10):
    """even sized U1 solution calculator"""

    m = int(n / 2 - 1)  # k, l size

    k = np.random.randint(1, m_max, size=m)
    l = np.random.randint(1, m_max, size=m)

    # generate plus and minus vector
    vp = np.concatenate(([l[0]], k, [-l[0]], -k))
    vm = np.concatenate(([0, 0], l, -l))

    # calculate z
    z = merge_op(vp, vm)

    return z, l, k


def odd(n, m_max=10):
    """odd sized U1 solution calculator"""

    m = int((n - 3) / 2)  # k, l size

    k = np.random.randint(1, m_max, size=m + 1)
    l = np.random.randint(1, m_max, size=m)

    # generate plus and minus vector
    up = np.concatenate(([0], k, -k))
    um = np.concatenate((l, [k[0], 0], -l, [-k[0]]))

    # calculate z
    z = merge_op(up, um)

    return z, l, k


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


def joint(n0, zmax=30, m_max=10):
    """main function to calculate quiral U1 solutions"""

    rs = 0  # aceptance variable - 0 is no-quiral, 1 is quiral

    while rs == 0:

        # gets z according to case
        if n0 % 2 == 0 and n0 > 2:
            zf, li, ki = even(n0, m_max)
        elif n0 % 2 != 0 and n0 >= 5:
            zf, li, ki = odd(n0, m_max)
        else:
            print("ingrese entero positivo válido")
            rs = 2
            break

        div = np.gcd.reduce(zf)  # finds z greater common divisor

        rs = no_vectorlike(zf)  # evaluates if z is vector-like

        # evaluates other conditions over z
        if rs == 1:
            zn = zf / div  # reduced z by its gcd
            if np.any(np.abs(zn) > zmax) or np.any(np.abs(zn) == 0):
                # all elements must be non zero and minor than 30
                rs = 0
                continue
            else:
                # return zn, l, k and gcd
                return (zn, li.tolist(), ki.tolist(), div)
                break


def multiple_sets(n, N=10100):
    n_values = np.full(N, n)
    pool = multiprocessing.Pool(4)
    start_time = time.perf_counter()
    result = pool.map(joint, n_values)
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")

    zs, z_inf = [], []
    for i in range(0, N):
        zs.append(result[i][0].tolist())
        z_inf.append(result[i][1:4])

    zs = np.array(zs)
    zs_uniq_quir, ind_zs = np.unique(np.sort(np.unique(zs, axis=0), axis=-1),
                                     axis=0, return_index=True)
    zs_inf = [z_inf[ind_zs[i]] for i in range(0, len(ind_zs))]
    return zs_uniq_quir, zs_inf


n_var = 6

final_zn, final_inf = multiple_sets(n_var)
final_zn = final_zn[~(np.isnan(final_zn).any(axis=1))]
final_inf = final_inf[0:len(final_zn)]

if n_var % 2 != 0 and n_var >= 5:
    uq_abs, zs_uni_indx = np.unique(np.sort(np.abs(final_zn)),
                                    return_index=True, axis=0)
    final_zn = final_zn[zs_uni_indx].copy()
    final_inf = [final_inf[zs_uni_indx[i]] for i in range(0, len(zs_uni_indx))]

for k in range(0, len(final_zn)):
    print(final_zn[k], final_inf[k])

print("total free anomaly sets: ", final_zn.shape[0])
