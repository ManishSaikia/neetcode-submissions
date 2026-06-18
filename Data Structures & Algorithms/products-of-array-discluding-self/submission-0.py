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

        # Case 1 : No Zeroes
        if zeroes == 0:
            for i in range(len(nums)):
                result[i] = product // nums[i]
        # Case 2 : 1 Zero
        if zeroes == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = product
        # Case 3 : 2 or more zeroes
        else:
            return result
        
        return result