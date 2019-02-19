if __name__ == '__main__':

    def go(size, serial):
        values = [[0 for i in range(size)] for j in range(size)]

        def hundreds(n): return (n // 100) % 10

        def value(x, y):  # 1-based
            rack_id = 10 + x
            return hundreds((rack_id * y + serial) * rack_id) - 5

        for i in range(size):
            for j in range(size):
                values[j][i] = value(i + 1, j + 1)

        m = -9999999999999
        mx, my = None, None
        for i in range(size - 2):
            for j in range(size - 2):
                s = sum(values[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
                if s > m:
                    m, mx, my = s, i + 1, j + 1
        print(m, my, mx)

    go(300, 7165)
