if __name__ == '__main__':
    WORKERS = 5
    def duration(ch): return 60 + ord(ch) - ord('A') + 1

    lines = open('input').read().strip().split('\n')
    nodes = set()
    deps = {}
    for l in lines:
        nodes = nodes.union({l[5], l[36]})
        deps[l[36]] = deps.get(l[36], set()).union({l[5]})

    for n in nodes:
        if n not in deps.keys():
            deps[n] = set()

    done = set()

    def peek_task(blacklist):
        possible = sorted(k for k, d in deps.items() if d.issubset(done) and k not in blacklist)
        return possible[0] if len(possible) else None

    def remove_task(n):
        del deps[n]

    sec = 0
    work = [None] * WORKERS
    already_assigned = set()
    while deps.keys():
        # finished tasks
        for i in range(len(work)):
            if work[i] is not None and work[i]['done'] == sec:
                remove_task(work[i]['task'])
                already_assigned.remove(work[i]['task'])
                done.add(work[i]['task'])
                work[i] = None

        # assign new tasks
        for i in range(len(work)):
            if not work[i]:
                t = peek_task(already_assigned)
                if t:
                    work[i] = {'task': t, 'done': sec + duration(t)}
                    already_assigned.add(t)
                else:
                    break

        print(sec, work, already_assigned, deps)
        sec += 1

    print(sec - 1)
