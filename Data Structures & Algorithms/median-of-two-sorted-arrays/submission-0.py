class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #brute force
        l1 = 0
        l2 = 0

        temp = []

        while(l1 < len(nums1) or l2 < len(nums2)):
            if(l1 == len(nums1)):
                for i in range(l2, len(nums2)):
                    temp.append(nums2[i])
                break
            
            elif(l2 == len(nums2)):
                for i in range(l1, len(nums1)):
                    temp.append(nums1[i])
                break
            
            else:
                if nums1[l1] > nums2[l2]:
                    temp.append(nums2[l2])
                    l2+=1
                elif (nums1[l1] < nums2[l2]):
                    temp.append(nums1[l1])
                    l1+=1
                else:
                    temp.append(nums1[l1])
                    temp.append(nums2[l2])
                    l1 +=1
                    l2 +=1 
        
        length = len(temp)
        if length%2 == 0:
            ret = temp[length//2] + temp[(length//2) - 1]
            return (ret/2)
        else:
            return temp[(length//2)]
        
                