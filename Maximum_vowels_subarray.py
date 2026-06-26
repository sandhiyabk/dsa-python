class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = set("aeiou")

        # Count vowels in the first window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maximum = count

        left = 0

        # Slide the window
        for right in range(k, len(s)):

            # Remove the left character
            if s[left] in vowels:
                count -= 1

            left += 1

            # Add the new right character
            if s[right] in vowels:
                count += 1

            # Update answer
            maximum = max(maximum, count)

        return maximum
