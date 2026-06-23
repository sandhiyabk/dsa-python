class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in mapping:
                if not stack:
                    return False
                top = stack.pop()
                if top != mapping[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
