def go(goal):
    scores = '37'
    e1, e2 = 0, 1

    while goal not in scores[-10:]:
        scores += str(int(scores[e1]) + int(scores[e2]))
        e1 = (e1 + 1 + int(scores[e1])) % len(scores)
        e2 = (e2 + 1 + int(scores[e2])) % len(scores)
    print(scores.index(goal))


if __name__ == '__main__':
    go('190221')
