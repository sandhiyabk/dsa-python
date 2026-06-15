class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())  #isalnum() for keeps only letters and digits and convert into lowercase if it is either char or num and finally join all together
        left=0
        right=len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
