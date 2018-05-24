# encoding=utf-8

import numpy as np
import os

class SimplexModel:

    def __init__(self, A, b, c):
        # initialize the model

        self._A = np.mat(A, dtype=float)  # xi shu ju zhen
        self._b = np.mat(b, dtype=float)  # fei qi ci xiang
        self._c = np.mat(c, dtype=float)  # max z 的系数
        self._c_index = zip(c, range(0, len(c)))  # max z 的系数与下标的绑定
        self._base = []  # ji

        for c_temp, index in self._c_index:
            if c_temp == 0:
                self._base.append(index)

        self._cb = [0 for temp in self._b.tolist()[0]]  # Cb initial
        self._cj_zj = c  # cj-zj
        self._cj_zj_index = zip(self._cj_zj,
                                range(0, len(self._cj_zj)))  #
        self.b_temp = []
        self.result = {}
        self.result_list = []

    def max_cjzj(self):
        # find the max of cj-zj with index

        self._cj_zj_index = zip(self._cj_zj,
                                range(0, len(self._cj_zj)))
        return max(self._cj_zj_index)

    def step_1(self):
        # b/xn
        # find the min line

        tar_cjzj, tar_colum = self.max_cjzj()

        if tar_cjzj <= 0:
            for i in range(len(self._cj_zj)):
                self.result['x%d' % (i + 1)] = 0
            for i, j in zip(self._base, range(len(self._base))):
                self.result['x%d' % (i+1)] = self._b.tolist()[0][j]
            for i, j in sorted(zip(self.result.keys(), self.result.values())):
                self.result_list.append(j)
            print(self.result)
            print("z = %f" % (np.mat(self.result_list, dtype=float) * np.mat(self._c, dtype=float).T))
            os._exit(1)

        b_list = self._b.tolist()[0]
        A_tar_list = [self._A[:, tar_colum].tolist()[i][0]
                      for i in range(len(self._A[:, tar_colum]))]

        for i, bi, xi in zip(range(0, len(b_list)), b_list, A_tar_list):  # b / xn
            try:
                # self._b[0, i] = bi / xi
                self.b_temp.append(bi / xi)
            except ZeroDivisionError:
                self.b_temp.append(999999)

        # find the minimum of b column as well as it's index
        # b_min, b_index = min(zip(self._b.tolist()[0], range(len(self._b.tolist()[0]))))
        b_min, b_index =min(zip(self.b_temp, range(len(self.b_temp))))
        self.b_temp = []
        return tar_cjzj, tar_colum, b_min, b_index

    def step_2(self):
        # replace the base
        # replace the Cb

        tar_cjzj, tar_colum, b_min, b_index = self.step_1()
        main_element = self._A[b_index, tar_colum]
        self._base[b_index] = tar_colum  # update the base
        self._cb[b_index] = tar_cjzj  # update the Cb
        # self._cj_zj[tar_colum] = 0  # clear the element

        # main element line multiplied to one
        # other lines subscribed to zero

        main_line = self._A[b_index, :]
        main_line = main_line / main_element
        self._A[b_index, :] = main_line
        self._b[0, b_index] = self._b[0, b_index] / main_element

        for i in range(len(self._A)):
            if i == b_index:
                continue
            temp_1 = self._A[i, tar_colum]
            self._A[i, :] = self._A[i, :] - temp_1 * main_line
            self._b[0, i] = self._b[0, i] - temp_1 * self._b[0, b_index]

        self._cj_zj = (self._cj_zj - self._cj_zj[tar_colum] * main_line).tolist()[0]

        self.step_2()

