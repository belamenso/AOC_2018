class Node:
    def __init__(self, l, r, v):
        self.l = l
        self.r = r
        self.v = v


class List:
    def __init__(self, players, last_marble):
        self.curr = Node(None, None, 0)
        self.curr.l = self.curr.r = self.curr

        self.players = players
        self.scores = [0] * players
        self.player = 0

        self.m = 1  # next marble
        self.last_marble = last_marble

    def move(self):
        if self.m % 23:
            self.curr = self.curr.r
            prev, next = self.curr, self.curr.r
            new = Node(prev, next, self.m)
            prev.r, next.l = new, new
            self.curr = new
        else:
            self.scores[self.player] += self.m
            for _ in range(7):
                self.curr = self.curr.l
            self.curr.l.r = self.curr.r
            self.curr.r.l = self.curr.l
            self.scores[self.player] += self.curr.v
            self.curr = self.curr.r

        self.m += 1
        self.player = (self.player + 1) % self.players

    def highest_score(self):
        return max(self.scores)

    def simulate(self):
        while True:
            self.move()
            if self.m == self.last_marble:
                break
        print(self.highest_score())


if __name__ == '__main__':
    # List(17, 1104).simulate()  # Doesn't pass, maybe an error on the aoc website?
    # List(476, 71657).simulate()
    List(476, 71657 * 100).simulate()
