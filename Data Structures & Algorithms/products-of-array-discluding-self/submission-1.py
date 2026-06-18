class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        zeroes = 0
        product = 1

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num
        
        # case 1 : No 0 
        if zeroes == 0:
            for i in range(len(nums)):
                result[i] = product // nums[i]
            return result
        # case 2 : 1 zero
        if zeroes == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = product
            return result
        # case 3 : 2 or more zeroes

        return result