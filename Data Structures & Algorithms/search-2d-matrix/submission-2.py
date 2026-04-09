class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr: List[int], target: int) -> bool:
            l=0
            r=len(arr)-1

            while(l<=r):
                mid = l + ((r-l)//2)
                if(arr[mid]==target):
                    return True
                elif(arr[mid] < target):
                    l+=1
                else:
                    r-=1
            return False
        
        row = []
        last = len(matrix[0]) - 1
        for i in matrix:
            if(target<=i[last]):
                row = i
                break
        print(row)
        if(row==[]):
            return False

        return binSearch(row, target)
    