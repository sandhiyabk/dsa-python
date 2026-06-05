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
#the hashmap is using so that we can have value and it's index like 2:0 7:1 4:2 for better solution by using formula (remain=target-nums[i]) and check if remain in hashmap.
