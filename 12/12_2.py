initial = '##.#...#.#.#....###.#.#....##.#...##.##.###..#.##.###..####.#..##..#.##..#.......####.#.#..#....##.#'
generations = 100

if __name__ == '__main__':
    rules = {}
    for line in open('input').read().split('\n'):
        rules[line[:5]] = line[9]

    offset = 20
    gen = 0
    state = (['.'] * offset) + [c for c in initial] + (['.'] * 100)

    def move():
        global state, gen
        new_state = ['.'] * len(state)
        for i in range(2, len(state) - 2):
            new_state[i] = rules[''.join(state[i-2:i+3])]
        state = new_state
        gen += 1

    while gen != 90:
        move()
        print(gen, ''.join(state))
    gen90 = sum(i - offset for i, c in enumerate(state) if c == '#')
    plant_count = sum(c == '#' for c in ''.join(state))
    ret = gen90 + plant_count * (50000000000 - 90)
    print(ret)

