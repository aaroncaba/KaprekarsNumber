import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import cProfile


def digits_of(k: int, num_of_digits: int) -> npt.NDArray:
    ret = np.zeros(num_of_digits, dtype=np.int32)
    for i in range(num_of_digits):
        place = num_of_digits-i-1
        ret[i] = np.int32(k // 10**place % 10)

    return ret


def digits_bigf(k: int, num_of_digits: int):
    dd = digits_of(k, num_of_digits)
    tmp = -np.sort(-dd)
    return tmp


def digits_smallf(k: int, num_of_digits):
    dd = digits_of(k, num_of_digits)
    return np.sort(dd)


def digits_to_num(digits: npt.NDArray):
    nsmall = ''
    for dd in digits:
        nsmall += str(dd)
    return int(nsmall)


def iter_count(k: int, num_of_digits: int):
    knew = k
    kold = 0
    count = 0

    while kold != knew or count == 0:
        kold = knew
        nsmall = digits_to_num(digits_smallf(knew, num_of_digits))
        nbig = digits_to_num(digits_bigf(knew, num_of_digits))
        knew = nbig - nsmall
        count += 1
        if count > 1000:
            break

    return count-1, knew


def calc_it(n: int) -> None:
    cc = 10**n
    count = np.zeros(10**n, dtype=np.int32)
    final = np.zeros(10**n, dtype=np.int32)
    for i in range(1, cc):
        cc, ff = iter_count(i, n)
        count[i] = cc
        final[i] = ff
        if i / 100 == math.floor(i/100):
            print(i)
    return count, final


if __name__ == "__main__":
    n = 5

    # cProfile.run('calc_it(n)')

    count,final = calc_it(n)

    plt.figure(0)
    plt.plot(final)
    plt.figure(1)
    plt.plot(count)

    finalnum = list(set(final))
    print(finalnum)

    counts = set(count)
    print(count)
