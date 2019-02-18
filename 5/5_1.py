class Node:
    def __init__(self, l, r, v):
        self.l = l
        self.r = r
        self.v = v


def strToList(s):
    start = Node(None, None, s[0])
    last = start
    for i in range(1, len(s)):
        n = Node(last, None, s[i])
        last.r = n
        last = n
    return start


def react(s):

    ls = strToList(s)

    def opposite(a, b):
        for x, y in ((a,b), (b,a)):
            if x == x.lower() and y != y.lower(): return True
        return False

    def not_end(lst):
        return lst is not None and lst.r is not None

    c = ls
    start = c
    while not_end(c):
        if c.v.lower() == c.r.v.lower() and opposite(c.v, c.r.v):
            b = False
            if start == c:
                b = True
                start = c.r.r
            prev = c.l
            c = c.r.r
            c.l = prev
            if prev is not None:
                prev.r = c
                c = prev
            else:
                assert b  # needed to be sure this would work
                c = start
        else:
            c = c.r

    s = ''
    c = start
    while c is not None:
        s += c.v
        c = c.r

    return s


if __name__ == '__main__':
    s = open('input').read()
    print(len(react(s)))
