#!/usr/bin/python3

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        height: int = len(board) - 1
        width: int = len(board[0]) - 1
        exist: list[bool] = [False]

        def recursive(coord, seen={}, index=0):

            print(coord)

            if exist[0]:
                return

            if coord[0] < 0 or coord[1] < 0:
                return

            if coord[0] > height or coord[1] > width:
                return

            if seen.get((coord[0], coord[1])) is not None:
                return

            if index == len(word):
                return

            if board[coord[0]][coord[1]] == word[index]:
                if index == 0:
                    seen = {}

                print("reached", word[index], seen)
                seen[(coord[0], coord[1])] = True
                index += 1

                if index == len(word):
                    exist[0] = True
                    return

            else:
                if index == 0:
                    seen[(coord[0], coord[1])] = False

                # no deberia llamar dos veces seguidas a las funciones
                # es decir, tiene que tener una letra igual pegada
                if index != 0:
                    return

            recursive(self.move_up([coord[0], coord[1]]), seen, index)
            recursive(self.move_right([coord[0], coord[1]]), seen, index)
            recursive(self.move_down([coord[0], coord[1]]), seen, index)
            recursive(self.move_left([coord[0], coord[1]]), seen, index)

        recursive([0, 0])

        return exist[0]

    def move_up(self, coord):

        return [coord[0] - 1, coord[1]]

    def move_right(self, coord):

        return [coord[0], coord[1] + 1]

    def move_down(self, coord):

        return [coord[0] + 1, coord[1]]

    def move_left(self, coord):

        return [coord[0], coord[1] - 1]


obj = Solution()

print(obj.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
