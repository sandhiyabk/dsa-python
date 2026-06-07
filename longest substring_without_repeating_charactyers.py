class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen=set()
        left=0
        maximum=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maximum=max(maximum,right-left+1)
        return maximum
#In brute force by myself it doesn't pass for 3rd test case.so i have to use the optimal solution which is "Sliding window"-in that the logic involves if the element already present in seen set the old will be removed and new will be added so that the 3rd case ("pwwkew") will be passed and efficient by space and time complexity.
