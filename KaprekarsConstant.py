import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import cProfile


class KaprekaersConstant():
    def __init__(self, n):
        self.n = n
        self.zeros = np.zeros(n, dtype=np.int32)

    def digits_of(self, k: int,  type: str):
        # get individual digits
        digits = self.zeros.copy()
        s = str(k)
        for i in range(len(s)):
            digits[i] = int(s[i])

        if type == 'big':
            digits[::-1].sort()
        elif type == 'small':
            digits.sort()
        else:
            raise Exception(f'Badd Argument:  {type}')

        return digits

    def digits_to_num(self, digits: npt.NDArray):
        m = 1
        ret = 0
        for dd in digits[::-1]:
            ret = ret + m*dd
            m = m*10
        return ret

    def iter_count(self, k: int ):
        knew = k
        kold = 0
        count = 0
        klist = [k]

        while kold != knew or count == 0:
            kold = knew
            nsmall = self.digits_to_num(
                self.digits_of(knew,  type='small'))
            nbig = self.digits_to_num(self.digits_of(
                knew,  type='big'))
            knew = nbig - nsmall
            count += 1
            # print(count, kold)

            if knew in klist:
                break
            klist.append(knew)

        return count-1, knew

    def calc_it(self,  max_n=None) -> None:
        if max_n is None:
            max_n = 10**self.n-1
        max_n = min(max_n, (10**self.n)-1)
        count = np.zeros(max_n+1, dtype=np.int32)
        final = np.zeros(max_n+1, dtype=np.int32)
        for i in range(1, max_n+1):
            cc, ff = self.iter_count(i)
            count[i] = cc
            final[i] = ff
            if i / 1000 == math.floor(i/1000):
                print(i)
        return count, final


if __name__ == "__main__":

    num_of_digits = 6
    profile = True

    kc = KaprekaersConstant(num_of_digits)

    if profile:
        cProfile.run('kc.calc_it(100000)', sort='tottime')
    else:
        count, final = kc.calc_it(10**5)
        plt.figure(0)
        plt.plot(final)
        plt.figure(1)
        plt.plot(count)

        finalnum = np.unique(final)
        print(f'Last numbers: {finalnum}')

        counts = np.unique(count)
        print(f'Cycle counts: {counts}')
