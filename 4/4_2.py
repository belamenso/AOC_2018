lines = [line for line in open('input').read().split('\n')]
lines.sort(key=lambda line: line[6:17])


def go():
    sleeping_times = {}

    current_num = 0
    start = 0
    for l in lines:
        log = l[19:]
        if '#' in log:
            current_num = int(log[7:7+log[7:].index(' ')])
        else:
            minute = int(l[15:17])
            if 'asleep' in log:
                start = minute
            else:  # awakening
                if current_num not in sleeping_times.keys():
                    sleeping_times[current_num] = {m: 0 for m in range(60)}
                for m in range(start, minute):
                    sleeping_times[current_num][m] += 1
    m = 0
    selected_guard = -1
    for k, v in sleeping_times.items():
        print(k, max(v.values()), v.values())
        if max(v.values()) > m:
            m = max(v.values())
            selected_guard = k
    ret = m * selected_guard
    print(m, selected_guard)
    print(ret)


if __name__ == '__main__':
    go()
