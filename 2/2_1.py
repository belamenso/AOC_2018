if __name__ == '__main__':
    count2, count3 = 0, 0
    for word in open('input').read().strip().split('\n'):
        counts = {}
        for char in word:
            counts[char] = counts.get(char, 0) + 1
        if 2 in counts.values(): count2 += 1
        if 3 in counts.values(): count3 += 1
    print(count2 * count3)
