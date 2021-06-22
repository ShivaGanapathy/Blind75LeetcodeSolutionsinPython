class Solution:
    #O(n^2) approach
    def maxProfit1(self, prices):
        profit = 0
        for i in range(len(prices)):
            current = prices[i]
            for j in range(i+1,len(prices)):
                if (prices[j] - current)>profit:
                    profit = prices[j] - current
                    print(i,j)
        return profit

    #O(n) approach
    def maxProfit2(self, prices):
        lp,rp,profit = 0,1,0
        
        for i in range(len(prices)):
            if prices[rp]>prices[lp]:
                if prices[rp]-prices[lp]>profit:
                    profit = prices[rp]-prices[lp]
                rp+=1
                    
            else:
                lp = rp
                rp+=1
        return profit
        
        
                