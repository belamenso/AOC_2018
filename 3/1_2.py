if __name__ == '__main__':

    inches = {(x, y): (0, None) for x in range(1001) for y in range(1001)}
    claims = {}

    for line in open('input').read().split('\n'):
        num = int(line[1:line.index('@')])
        x, y = map(int, line[line.index('@')+1:line.index(':')].split(','))
        dx, dy = map(int, line[line.rindex(':')+1:].split('x'))

        claims[num] = (x, y, dx, dy)

        for da in range(dx):
            for db in range(dy):
                at = (x + da + 1, y + db + 1)
                inches[at] = inches.get(at)[0] + 1, num

    failed_candidates = set()
    for inch in inches:
        if inch[0] == 1:
            candidate = inch[1]
            if candidate not in failed_candidates and candidate != 0:
                try:
                    for da in range(claims[candidate][2]):
                        for db in range(claims[candidate][3]):
                            at = (claims[candidate][0] + da + 1, claims[candidate][1] + db + 1)
                            assert inches[at][0] == 1
                    print(candidate)
                    exit()
                except AssertionError:
                    failed_candidates.add(candidate)
