# 2022. Convert 1D Array Into 2D Array
# Answer
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        if m*n==len(original):
            a=0
            for i in range(0,m):
                t=[]
                for j in range(0,n):
                    t.append(original[a])
                    a=a+1
                ans.append(t)
            #return ans
        return ans


# 1954. Minimum Garden Perimeter to Collect Enough Apples
# Answer
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def calcApples(R):
            return 2 * R * (R + 1) * (2 * R + 1)
        
        left = 1
        right = 100000
        minR = 1
        while left <= right:
            mid = (left + right) // 2
            if calcApples(mid) >= neededApples:
                minR = mid
                right = mid - 1
            else:
                left = mid + 1
        return minR * 8


# 1935. Maximum Number of Words You Can Type
# Answer
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = list(brokenLetters)
        lst = text.split()
        result = 0
        for word in lst:
            found_broken = False
            for b in broken:
                if b in word:
                    found_broken = True
                    break  # Exit the inner loop if a broken letter is found in the word
            if not found_broken:
                result += 1
        return result



        