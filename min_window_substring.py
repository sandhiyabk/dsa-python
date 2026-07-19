class Solution(object):
    def minWindow(self, s, t):
        #t-frequency count
        target = {} 

        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        #s where t present inclution-frequency count
        window = {}

        have = 0
        need = len(target)

        left = 0

        min_len = float('inf') #the inf meands infinite postive maximaum number
        result = "" #final result storage

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1 #frequency count of s
            #if char present in target then have +1
            if char in target and window[char] == target[char]:
                have += 1 
            #once have and needed satisfied find min length then remove leftmost element fo further checking
            while have == need:

                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right + 1]

                window[s[left]] -= 1
                #while removing left and the taget's element is reducing have will less-1
                if (s[left] in target and
                    window[s[left]] < target[s[left]]): # for sometimes the taget element duplicates can be in s only if window[x:1] removing then have less-1
                    have -= 1

                left += 1 #next iteration

        return result
