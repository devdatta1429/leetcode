# class Solution(object):
#     def coinChange(self, coins, amount):
#         dp =[amount + 1] * (amount + 1)
#         dp[0] = 0
        
#         for i in range(1, amount+1):
#             for coin in coins:
#                 if coin <=i :
#                     dp[i] = min(dp[i], dp[i - coin] + 1)

#         if dp[amount] == amount+1:
#             return -1
#         return dp[amount]

# # code is using a Greedy approach choose the largest coin possible, subtract it, and increase count.
# # Greedy doesn't always give the minimum number of coins for LeetCode 322.
# # Your code corrected (Greedy approach)

#         # count = 0
#         # coins.sort(reverse=True)

#         # for coin in coins:
#         #     while amount >= coin:
#         #         amount -= coin
#         #         count += 1

#         # if amount == 0:
#         #     return count
#         # else:
#         #     return -1



class Solution:
    def coinChange(self, coins, amount):
        memo = {}

        def solve(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            if amount in memo:
                return memo[amount]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + solve(amount - coin))

            memo[amount] = ans
            return ans

        result = solve(amount)

        return result if result != float('inf') else -1
