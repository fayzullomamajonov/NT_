# 2103. Rings and Rods
# Answer
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for n in range(0, len(rings), 2):
            r, p = rings[n], rings[n + 1]
            rods[int(p)].add(r)

        total = 0
        for r in rods:
            if len(r) == 3:
                total += 1

        return total


# 2108. Find First Palindromic String in the Array
# Answer
class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def firstPalindrome(self, words):
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""


# 2114. Maximum Number of Words Found in Sentences
# Answer
class Solution:
    def mostWordsFound(self, sentences) -> int:
        m = 0
        for i in sentences:
            c = 0
            for j in i:
                if j == " ":
                    c += 1
            m = max(m, c + 1)
        return m
