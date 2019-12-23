# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n 
        while l <= r:
            mid = (l + r)//2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid - 1):
                r = mid - 1
            elif not isBadVersion(mid):
                l = mid + 1
        return None
