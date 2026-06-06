class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        best_max=nums[0]
        for j in range(1,len(nums)):
            sum=max(nums[j], sum + nums[j])
            best_max = max(best_max, sum)
        return best_max
#in o(n):always check if current index value is greater than max if it is don't waste time use sum+=max(nums[i],sum+nums[i])
