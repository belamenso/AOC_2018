if __name__ == '__main__':

    def go(size, serial):
        values = [[0 for _ in range(size)] for _ in range(size)]

        def hundreds(n): return (n // 100) % 10

        def value(x, y):  # 1-based
            rack_id = 10 + x
            return hundreds((rack_id * y + serial) * rack_id) - 5

        for i in range(size):
            for j in range(size):
                values[j][i] = value(i + 1, j + 1)

        m = -9999999999999
        ml, mr, mt, mb = (None,) * 4

        tmp = [0] * size
        for L in range(size):
            for R in range(L, size):
                if R == L:
                    tmp = [0] * size
                for i in range(size):
                    tmp[i] += values[i][R]

                block_size = R - L + 1
                _m, _t, _b = sum(tmp[:block_size]), 0, block_size - 1
                _curr_sum = _m
                for i in range(1, len(tmp) - block_size + 1):
                    _curr_sum += tmp[i + block_size - 1] - tmp[i - 1]
                    if _curr_sum > _m:
                        _m, _t, _b = _curr_sum, i, i + block_size - 1
                if _m > m:
                    m, ml, mr, mt, mb = _m, L + 1, R + 1, _t + 1, _b + 1

        print(m, ml, mr, mt, mb)
        print(ml, mt, mr - ml + 1, sep=',')

    go(300, 7165)
