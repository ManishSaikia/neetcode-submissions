class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2
        if len(B)<len(A):
            A,B=B,A
        left,right=0,len(A)-1
        while True:
            midA=(left+right)//2
            midB=half-midA-2
            leftA=A[midA] if midA>=0 else float('-inf')
            leftB=B[midB] if midB>=0 else float('-inf')
            rightA=A[midA+1] if midA+1<len(A) else float('inf')
            rightB=B[midB+1] if midB+1<len(B) else float('inf')
            if leftA<=rightB and leftB<=rightA:
                if total%2:
                    return min(rightA,rightB)
                return (max(leftA,leftB)+min(rightA,rightB))/2
            elif leftA<rightB:
                left=midA+1
            else:
                right=midA-1