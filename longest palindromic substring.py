class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        start, end = 0, 0
        def expand_around_center(left, right): #expand around center to find the palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]: #untile same
                left -= 1 # left decrease
                right += 1 #right increase
            return left + 1, right - 1 #because of last left and right expansion are not crt return left+1 and right-1
        for i in range(len(s)):
            l1, r1 = expand_around_center(i, i) #odd index same index for left and right
            if (r1 - l1) > (end - start): #if new palindrom is largest make that index strart and end.to find length we always put like left-right+1 but here no need for +1
                start, end = l1, r1
            l2, r2 = expand_around_center(i, i + 1) #even index left=i right=i+1
            if (r2 - l2) > (end - start): #if new palindrom is largest make that index strart and end.to find length we always put like left-right+1 but here no need for +1
                start, end = l2, r2
        return s[start:end + 1]
