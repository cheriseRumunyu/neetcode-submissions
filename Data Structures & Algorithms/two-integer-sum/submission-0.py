class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            j = i +1
            while j < len(nums):
                if nums[i] +nums[j] == target:
                    ans.append([i, j])
                j +=1
        return ans[0]
