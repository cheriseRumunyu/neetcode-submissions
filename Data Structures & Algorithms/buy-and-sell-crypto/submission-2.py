class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
                
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

        # USING TWO POINTERS
        # l, r = 0, 1
        # maxP = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)

        #     else:
        #         l = r
        #     r += 1
        # return maxP
