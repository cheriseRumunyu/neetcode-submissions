class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_1 = sorted(nums)
        current = 1
        longest = 1

        for num in range(len(nums_1) - 1):
            difference = nums_1[num + 1] - nums_1[num]

            if difference == 1:
                current += 1
            elif difference == 0:
                continue
            else:
                current = 1

            longest = max(longest, current)

        return longest