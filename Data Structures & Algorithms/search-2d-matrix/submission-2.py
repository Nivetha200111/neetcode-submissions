from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Handle empty matrix edge case
        if not matrix or not matrix[0]:
            return False

        # Get dimensions of the matrix
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Start at the top-right corner
        row = 0
        col = num_cols - 1

        # Loop as long as our pointers are within the matrix bounds
        while row < num_rows and col >= 0:
            curr_ele = matrix[row][col]

            if curr_ele == target:
                return True  # Found it!
            
            # If target is smaller, the target can't be in this column. Move left.
            elif target < curr_ele:
                col -= 1
            
            # If target is larger, the target can't be in this row. Move down.
            else: # target > curr_ele
                row += 1
        
        # If the loop finishes, the target was not found
        return False