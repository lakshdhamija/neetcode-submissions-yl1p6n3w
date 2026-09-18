class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                topLeft = matrix[top][l + i] # save the topleft val
                matrix[top][l + i] = matrix[bottom - i][l] # move bottom left into top left
                matrix[bottom - i][l] = matrix[bottom][r - i] # move bottom right into bottom left
                matrix[bottom][r - i] = matrix[top + i][r] # move top right into bottom right
                matrix[top + i][r] = topLeft # move top left into top right
            l, r = l + 1, r - 1