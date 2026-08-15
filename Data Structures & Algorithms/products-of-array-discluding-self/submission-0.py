class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1

        #Left to right
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        #Right to left
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output