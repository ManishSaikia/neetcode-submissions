class Solution:
    def binarySearch(self, nums, left, right, target):
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return -1
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        min_index=left
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        min_index=left
        if min_index==0:
            return self.binarySearch(nums,0,len(nums)-1,target)
        elif nums[0]<=target<=nums[min_index-1]:
            return self.binarySearch(nums,0,min_index-1,target)
        else:
            return self.binarySearch(nums,min_index,len(nums)-1,target)