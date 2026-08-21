class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmap:
                return [hmap[comp], i]
            hmap[nums[i]] = i