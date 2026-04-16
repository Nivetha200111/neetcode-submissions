class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        nurow = len(matrix)
        nucol = len(matrix[0])
        r = 0
        c = len(matrix[0])-1
        while r < nurow and c >=0:
            currele = matrix[r][c]
            if currele == target:
                return True
            if currele < target:
                r += 1
            else:
                c-=1
        return False