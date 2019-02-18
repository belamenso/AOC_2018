if __name__ == '__main__':
    inches = {(x, y): 0 for x in range(1001) for y in range(1001)}
    for line in open('input').read().split('\n'):
        x, y = map(int, line[line.index('@')+1:line.index(':')].split(','))
        dx, dy = map(int, line[line.rindex(':')+1:].split('x'))
        for da in range(dx):
            for db in range(dy):
                inches[(x + da + 1, y + db + 1)] += 1
    count = 0
    for x in inches.values():
        if x >= 2: count += 1
    print(count)
