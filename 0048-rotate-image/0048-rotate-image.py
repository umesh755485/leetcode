class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse_rows(self, matrix):
        for row in matrix:
            row.reverse()

    def rotate(self, matrix):
        self.transpose(matrix)
        self.reverse_rows(matrix)