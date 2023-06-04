def maxProfit(self,prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if len(prices) == 0:
        return 0

    minPrice = prices[0]
    maxProfit = 0

    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        else:
            maxProfit = max(maxProfit, prices[i] - minPrice)

    return maxProfit