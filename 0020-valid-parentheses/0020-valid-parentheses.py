class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {')':'(', ']':'[', '}':'{'}
        for l in s:
            if l in "([{":
                stack.append(l)
            elif not stack or stack[-1] != hm[l]:
                return False
            else:
                stack.pop()

        return True if len(stack) == 0 else False