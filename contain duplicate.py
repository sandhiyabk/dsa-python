class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
#even after you check you always add the value in a new set 
#Best optimal solution is:return len(nums)!=len(set(nums))
