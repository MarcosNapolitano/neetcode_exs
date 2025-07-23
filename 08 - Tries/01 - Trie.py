#!/usr/bin/python3

class Node:

    def __init__(self):

        self.index = [None] * 26
        self.character = None
        self.word = False


class Trie:

    def __init__(self):

        self.index = [None] * 26

    def insert(self, word: str) -> None:

        curr = self.index
        lastnode = None

        for i in word:

            index = ord(i) - ord("a")

            if not curr[index]:
                curr[index] = Node()
                curr[index].character = i

            lastnode = curr[index]
            curr = curr[index].index

        lastnode.word = True

        return None

    def search(self, word: str) -> bool:

        curr = self.index
        lastnode = None

        for i in word:

            index = ord(i) - ord("a")

            if not curr[index]:
                return False

            if curr[index].character == i:
                lastnode = curr[index]
                curr = curr[index].index

        if lastnode.word:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:

        curr = self.index

        for i in prefix:

            index = ord(i) - ord("a")

            if not curr[index]:
                return False

            if curr[index].character == i:
                curr = curr[index].index

        return True


trie = Trie()
trie.insert("test")
print(trie.startsWith("tes"))
