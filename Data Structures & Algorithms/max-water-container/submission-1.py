class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # BRUTE FORCE  O(n^2)

        # best = 0
        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l],heights[r])
        #         best = max(best, area)
        
        # return best

        # TWO POINTERS  O(n)
        first = 0
        last = len(heights) - 1
        best = 0

        while first < last:
            area = (last - first) * min(heights[first], heights[last])
            best = max(best, area)

            if heights[first] < heights[last]:
                first += 1
            else:
                last -= 1
        return best


