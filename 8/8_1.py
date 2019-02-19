if __name__ == '__main__':
    data = [int(x) for x in open('input').read().split(' ')]

    def sum_metadata(i):
        children, metadata = data[i:i+2]
        i += 2

        s = 0
        for _ in range(children):
            s1, i = sum_metadata(i)
            s += s1

        s += sum(data[i:i+metadata])
        i += metadata

        return s, i

    print(sum_metadata(0)[0])
