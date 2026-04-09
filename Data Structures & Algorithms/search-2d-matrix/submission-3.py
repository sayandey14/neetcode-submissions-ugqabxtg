class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])

        l=0
        r = (row_len*col_len) - 1

        while (l<=r):
            mid = l + ((r-l)//2)

            row = mid // col_len
            col = mid % col_len

            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] > target):
                r = mid - 1
            else:
                l = mid + 1
        
        return False
    