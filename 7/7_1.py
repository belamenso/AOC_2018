if __name__ == '__main__':
    lines = open('input').read().strip().split('\n')
    nodes = set()
    deps = {}
    for l in lines:
        nodes = nodes.union({l[5], l[36]})
        deps[l[36]] = deps.get(l[36], set()).union({l[5]})

    for n in nodes:
        if n not in deps.keys():
            deps[n] = set()

    done = []
    while deps.keys():
        one_pass = sorted(k for k in deps.keys() if deps[k].issubset(set(done)))
        done.extend(one_pass[0])
        del deps[one_pass[0]]

    print(''.join(done))
