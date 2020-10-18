class Puzzle:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.puzzle = [[]]
        self.generate_grid()
        self.rule = ["down", "right", "up", "left"]

    def generate_grid(self):
        self.puzzle = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def go(self, path: list):
        width = height = 10
        i = self.start[0]
        j = self.start[1]
        goal_i = self.end[0]
        goal_j = self.end[1]
        while i != goal_i or j != goal_j:
            if i < height - 1 and self.puzzle[i+1][j] == 0:
                self.puzzle[i][j] = 1
                i += 1
                path.append([i, j])
            elif j < width - 1 and self.puzzle[i][j+1] == 0:
                self.puzzle[i][j] = 1
                j += 1
                path.append(([i, j]))
            elif i > 0 and self.puzzle[i-1][j] == 0:
                self.puzzle[i][j] = 1
                i -= 1
                path.append([i, j])
            elif j > 0 and self.puzzle[i][j-1] == 0:
                self.puzzle[i][j] = 1
                j -= 1
                path.append([i, j])


if __name__ == "__main__":
    p = Puzzle((0, 0), (3, 6))
    path = []

    p.go(path)
    print(path)