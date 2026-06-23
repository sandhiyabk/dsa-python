class Solution(object):
    def minWindow(self, s, t):

        target = {}

        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        window = {}

        have = 0
        need = len(target)

        left = 0

        min_len = float('inf')
        result = ""

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:

                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right + 1]

                window[s[left]] -= 1

                if (s[left] in target and
                    window[s[left]] < target[s[left]]):
                    have -= 1

                left += 1

        return result
