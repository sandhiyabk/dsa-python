class Solution:
    def two_sum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            a=target-nums[i]
            if a in seen:
                return [seen[a],i]
            seen[nums[i]]=i
s=Solution()
print(s.two_sum([2,7,11,15],9))
