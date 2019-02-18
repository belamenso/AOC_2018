lines = [line for line in open('input').read().split('\n')]
lines.sort(key=lambda line: line[6:17])

def determine_guard():
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
                sleeping_times[current_num] = sleeping_times.get(current_num, 0) + (minute - start)
    m = max(sleeping_times.values())
    for k, v in sleeping_times.items():
        if v == m:
            return k


def choose_minute(guard):
    proper_guard = False
    mins = {m: 0 for m in range(0, 60)}
    start = 0
    for l in lines:
        if '#' + str(guard) in l:
            proper_guard = True
        elif '#' in l:
            proper_guard = False
        elif proper_guard:
            minute = int(l[15:17])
            if 'asleep' in l:
                start = minute
            else:
                for m in range(start, minute):
                    mins[m] = mins.get(m) + 1
    ms = list(mins.items())
    ms.sort(key=lambda x: x[1], reverse=True)
    return ms[0][0]


if __name__ == '__main__':
    guard = determine_guard()
    m = choose_minute(guard)
    print(m * guard)
