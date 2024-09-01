import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import cProfile


def digits_of(k: int, num_of_digits: int):
    ret = np.zeros(num_of_digits, dtype=np.int32)
    s = str(k)
    for i in range(len(s)):
        ret[i] = int(s[i])
        # print(ret)

    return ret


def digits_bigf(k: int, num_of_digits: int):
    dd = digits_of(k, num_of_digits)
    tmp = -np.sort(-dd)
    return tmp


def digits_smallf(k: int, num_of_digits):
    dd = digits_of(k, num_of_digits)
    return np.sort(dd)


def digits_to_num(digits: npt.NDArray):
    m = 1
    ret = 0
    for dd in digits[::-1]:
        ret = ret + m*dd
        m = m*10
    return ret


def iter_count(k: int, num_of_digits: int):
    knew = k
    kold = 0
    count = 0
    klist = [k]

    while kold != knew or count == 0:
        kold = knew
        nsmall = digits_to_num(digits_smallf(knew, num_of_digits))
        nbig = digits_to_num(digits_bigf(knew, num_of_digits))
        knew = nbig - nsmall
        count += 1
        # print(count, kold)

        if knew in klist:
            break
        klist.append(knew)

    return count-1, knew


def calc_it(n: int, max_n=None) -> None:
    if max_n is None:
        max_n = 10**n-1
    max_n = min(max_n, (10**n)-1)
    count = np.zeros(max_n+1, dtype=np.int32)
    final = np.zeros(max_n+1, dtype=np.int32)
    for i in range(1, max_n+1):
        cc, ff = iter_count(i, n)
        count[i] = cc
        final[i] = ff
        if i / 1000 == math.floor(i/1000):
            print(i)
    return count, final


if __name__ == "__main__":

    n = 6

    profile = True
    if profile:
        cProfile.run('calc_it(n,10000)', sort='tottime')
    else:
        count, final = calc_it(n, 10**5)
        plt.figure(0)
        plt.plot(final)
        plt.figure(1)
        plt.plot(count)

        finalnum = np.unique(final)
        print(f'Last numbers: {finalnum}')

        counts = np.unique(count)
        print(f'Cycle counts: {counts}')
