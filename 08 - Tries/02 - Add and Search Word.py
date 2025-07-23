#!/usr/bin/python3

class Node:

    def __init__(self):
        self.index = {}
        self.word = None


class WordDictionary:

    def __init__(self):
        self.index = {}

    def addWord(self, word: str) -> None:

        curr = self.index
        lastnode = None

        for i in word:
            try:
                lastnode = curr[i]

            except KeyError:
                curr[i] = Node()
                lastnode = curr[i]

            curr = curr[i].index

        lastnode.word = True

    def search(self, word: str, index=None) -> bool:

        if index is None:
            curr = self.index
        else:
            curr = index

        lastnode = None

        for i in range(len(word)):

            if word[i] == ".":
                if curr.keys():
                    if i == len(word)-1:
                        for value in curr.values():
                            if value.word:
                                return True
                        return False

                    for key in curr.keys():
                        if self.search(word[i+1:], curr[key].index):
                            return True

                    return False

                else:
                    return False
            try:
                lastnode = curr[word[i]]
                curr = curr[word[i]].index

            except KeyError:
                return False

        if lastnode.word:
            return True

        return False


add = WordDictionary()

add.addWord("dad")
add.addWord("pad")
add.addWord("tad")
add.addWord("bad")
add.addWord('bat')

print(add.search("b."))
