# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
An analyst is analyzing a stock over a period of n days. The price of the stock on the th day is price[i], and the profit obtained is denoted by profit[i]. The analyst wants to pick a triplet of days (i, j, k) such that (i < j < k) and priceli] < price[il < price[k] in such a way that the total profit, i.e. profit[i] + profit[j] + profit[k] is maximized.
Find the maximum total profit possible. If there is no valid triplet, return -1.
Example
Consider n = 5, price = [1, 5, 3, 4, 6], profit = [2, 3, 4, 5, 6].
An optimal triplet (considering 1-based indexing)
is (3, 4, 5). Here 3 < 4 < 6, and total profit = 4 + 5 +
6 = 15, the maximum possible. So, the answer is
15.
Function Descriptian
Complete the function getMaximumProfit in the editor below.
getMaximumProfit has the following parameters:
int price[n]: the prices of the stock on each day int profit[n]: the

'''
def getMaximumProfit(price, profit):
    n = len(price)

    # Right max profit for a higher price
    max_profit_right = [0] * n
    max_price_from_right = price[n-1]

    for i in range(n-2, -1, -1):
        if price[i] < max_price_from_right:
            max_profit_right[i] = max(max_profit_right[i+1], profit[i+1])
        else:
            max_profit_right[i] = max_profit_right[i+1]
        max_price_from_right = max(max_price_from_right, price[i])

    # Left max profit for a lower price
    max_profit_left = [0] * n
    min_price_till_now = price[0]

    for j in range(1, n):
        if price[j] > min_price_till_now:
            max_profit_left[j] = max(max_profit_left[j-1], profit[j-1])
        else:
            max_profit_left[j] = max_profit_left[j-1]
        min_price_till_now = min(min_price_till_now, price[j])

    max_total_profit = -1
    for k in range(1, n-1):
        if max_profit_left[k] > 0 and max_profit_right[k] > 0:
            max_total_profit = max(max_total_profit, profit[k] + max_profit_left[k] + max_profit_right[k])

    return max_total_profit if max_total_profit > 0 else -1

# Test
price = [4,3,2,1]
profit = [4,3,2,1]
print(getMaximumProfit(price, profit))  # Expected output: -1

price =[2,3,1,5,9]
profit = [1, 2, 6, 1, 5]
print(getMaximumProfit(price, profit))#12