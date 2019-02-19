if __name__ == '__main__':
    data = [int(x) for x in open('input').read().split(' ')]

    def value(i):
        children, metadata = data[i:i+2]
        i += 2

        children_data = [0] * children
        for j in range(children):
            children_data[j], i = value(i)

        s = 0
        for _ in range(metadata):
            if children != 0:
                if 1 <= data[i] <= children:
                    s += children_data[data[i] - 1]
            else:
                s += data[i]
            i += 1

        return s, i

    print(value(0)[0])
