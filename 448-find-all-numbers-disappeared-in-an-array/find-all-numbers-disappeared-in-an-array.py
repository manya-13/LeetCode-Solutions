class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = max(nums)
        res = []
        for i in nums:
            
            idx = abs(i) - 1
            if nums[idx] < 0:
                continue
            nums[idx] *= -1
        
        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
        
        