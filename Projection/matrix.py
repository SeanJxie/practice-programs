"""

3xN matrix object and operations are defined here.

"""


def dot(v3_1, v3_2):
    # On the assumption that len(v3_1) == len(v3_2),
    return sum([v3_1[i] * v3_2[i] for i in range(len(v3_1))])


class M3xN:
    def __init__(self, n):
        self.n = n
        self._elems = [[0 for _ in range(n)] for _ in range(3)]

    def set_entire(self, m):
        self._elems = m

    def set(self, row, col, val):
        self._elems[row][col] = val

    def get(self, row, col):
        return self._elems[row][col]

    def _get_row(self, i):
        return self._elems[i]

    def _get_col(self, j):
        col = []
        for r in self._elems:
            col.append(r[j])
        return col

    def __repr__(self):
        return str(self._elems)

    def __mul__(self, o):
        if type(o) != M3xN:
            res_mat = self
            for i in range(3):
                for j in range(self.n):
                    res_mat.set(i, j, self._elems[i][j] * o)

        else:
            res_mat = M3xN(o.n)
            for i in range(3):
                for j in range(o.n):
                    row = self._get_row(i)
                    col = o._get_col(j)
                    res_mat.set(i, j, dot(row, col))

        return res_mat

    def __add__(self, m):
        res_mat = self

        for i in range(3):
            for j in range(self.n):
                res_mat.set(i, j, self._elems[i][j] + m.get(i, j))

        return res_mat

    def __sub__(self, m):
        res_mat = self

        for i in range(3):
            for j in range(self.n):
                res_mat.set(i, j, self._elems[i][j] - m.get(i, j))

        return res_mat
