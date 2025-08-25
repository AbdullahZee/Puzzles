class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        y = ''
        for a in x[::-1]:
            y += a
        if x == y:
            return True
        else:
            return False

print(Solution.isPalindrome('101'))