# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.






class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dic = {}
        dic[amount] = -1
        dic[0] = 0
        def recurse(index, amt, nums):
            nonlocal dic
            if index >= len(coins):
                return
            if amt in dic and dic[amt] != -1:
                return dic[amt]
            diff = amt-coins[index]
            if amt - coins[index] >= 0:
                dic[amt] = min(dic.get(amt, amount + 1), 1 + dic.get(amt-coins[index],amount + 1))
                return dic[amt]
            recurse(index,amt-coins[index]) 
            recurse(index+1,amt)  
                                                                                                     
        recurse(0, amount, 0)
        return dic[amount]


sol = Solution()
print(sol.coinChange([7,5,3], 13))

























































# def recurse(index: int, coins: [], amount: int, dp: {}):
#     if amount == 0:
#         return 1
#     if index >= len(coins):
#         return -1
#     key = str(amount) + "-" + str(index)
#     if key in dp:
#         return dp[key]
#     coin = 0
#     count = 0
#     while(coin <= amount):
#         rem = amount - coin
#         count += recurse(index + 1, coins, rem, dp)
#         coin += coins[index]
#     dp[key] = count
#     return count


        


# def coinChange(coins: [], amount: int) -> int:
#     dp = [amount+1]*(amount+1) 
#     dp[0] = 0
#     for k in range(0, amount+1):
#         for j in range(0, len(coins)):
#             if coins[j] <= k:
#                 dp[k] = min(dp[k], 1 + dp[k-coins[j]])

#     return dp[amount] if dp[amount] <= amount else -1
    


# coins = [5, 2, 1]
# amount = 11
# print(coinChange(coins, amount))


    # coin: int = coins[index]
    # if amount in dp:
    #     if dp[amount] > count +1:
    #         dp[amount] = count +1
    # else:
    #     for k in range(0, int(amount/coin) + 1):
    #         if k == 0:
    #             if index<len(coins) -1:

    #                 recurse(index +1, coins, amount, count)

    #         elif k == int(amount/coin):
    #             if index<len(coins)-1:
    #                 recurse(index +1 , coins, amount-coin*k, count +1)
    #             else:
    #                 if amount in dp:
    #                     if dp[amount] > count +1:
    #                         dp[amount] = count +1
    #                 else:
    #                     dp[amount] = count + 1
    #         else:
    #             if amount in dp:
    #                 if dp[amount] > count +1:
    #                     dp[amount] = count +1
    #             recurse(index, coins, amount - coin*k, count + 1)