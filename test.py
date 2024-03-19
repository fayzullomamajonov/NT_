# You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.

# Return an array that consists of indices of peaks in the given array in any order.

# Notes:

# A peak is defined as an element that is strictly greater than its neighboring elements.
# The first and last elements of the array are not a peak.


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                res.append(i)
        return res


# You are given a 0-indexed integer array coins, representing the values of the coins available, and an integer target.

# An integer x is obtainable if there exists a subsequence of coins that sums to x.

# Return the minimum number of coins of any value that need to be added to the array so that every integer in the range [1, target] is obtainable.

# A subsequence of an array is a new non-empty array that is formed from the original array by deleting some (possibly none) of the elements without disturbing the relative positions of the remaining elements.


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()

        extraCoins = reachable = 0
        for coin in coins:
            while reachable < (coin - 1):
                reachable = 2 * reachable + 1
                extraCoins += 1
            reachable += coin

        while reachable < target:
            reachable = 2 * reachable + 1
            extraCoins += 1

        return extraCoins


# You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively.

# Consider calculating the following values:

# The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
# The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.
# Return an integer array answer of size 2 containing the two values in the above order.

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        y = []
        cnt = 0
        c = 0
        j = []
        for i in nums1:
            if i in nums2:
                cnt += 1
            x.append(cnt)
        j.append(max(x))
        for i in nums2:
            if i in nums1:
                c += 1
            y.append(c)
        j.append(max(y))
        return j
