class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in freq:
                return [freq[comp],i]
            freq[nums[i]]=i