# 2413. Smallest Even Multiple
# Answer:
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            i = n+n
            return i
        
# 2418. Sort the People
# Answer:
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        c = {heights[i]: i for i in range(len(heights))}
        heights.sort()
        res = []
        for i in range(len(heights)-1, -1, -1):
            res.append(names[c[heights[i]]])
        return res       
    
# 2424. Longest Uploaded Prefix
# Answer:
class LUPrefix:

    def __init__(self, n: int):
        self.stream = [False]*n
        self.maxLength = n
        self.prefLength = 0
        
    def upload(self, video: int) -> None:
        self.stream[video-1] = True

    def longest(self) -> int:
        for i in range(self.prefLength,self.maxLength):

            if self.stream[i]:
                self.prefLength = i+1

            else: break

        return self.prefLength