class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]*len(nums)
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            res[i]=prefix
        return res
