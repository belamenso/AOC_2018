if __name__ == '__main__':
    words = set()
    for word in open('input').read().strip().split('\n'):
        for i in range(len(word)):
            smaller_word = word[:i] + word[i + 1:]
            if (smaller_word, i) in words:
                print(smaller_word)
                exit()
            else:
                words.add((smaller_word, i))
