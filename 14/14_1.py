def digits(n):
    return [int(c) for c in str(n)]


def go(goal):
    scores = [3, 7] + [0] * 1000
    e1, e2 = 0, 1
    size = 2

    while size < goal + 10:
        ds = digits(scores[e1] + scores[e2])
        scores[size:size+len(ds)] = ds
        size += len(ds)
        e1 = (e1 + 1 + scores[e1]) % size
        e2 = (e2 + 1 + scores[e2]) % size

    print(*scores[goal:goal+10], sep='')


if __name__ == '__main__':
    go(190221)
