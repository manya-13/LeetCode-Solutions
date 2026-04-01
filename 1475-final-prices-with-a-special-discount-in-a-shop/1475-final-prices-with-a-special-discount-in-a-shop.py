class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        if len(prices) <= 1:
            return prices

        j = 0
        
        for i in range(1, len(prices)):
            if prices[i] <= prices[j]:
                prices[j] = prices[j] - prices[i]
            else:
                k = i + 1
                while k <= len(prices) - 1:
                    if prices[k] > prices[j]:
                        k+=1
                        continue
                    else:
                        prices[j] = prices[j] - prices[k]
                        break
            res.append(prices[j])
            j+=1
        res.append(prices[len(prices)-1])
        return res
