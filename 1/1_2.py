if __name__ == '__main__':
    deltas = [int(line) for line in open('input').read().strip().split('\n')]
    i, curr = 0, 0
    seen = {curr}
    while True:
        d = deltas[i % len(deltas)]
        curr += d
        if curr in seen:
            print(curr)
            break
        else:
            seen.add(curr)
        i += 1
