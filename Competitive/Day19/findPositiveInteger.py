class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        lst = list(range(1, z + 1))
        for i in lst:
            temp = self.binarySearch(customfunction, lst, z, i)
            if temp != -1:
                ans.append([temp, i])
        return ans
        
    def binarySearch(self, customfunction, nums, z, x):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r)//2
            temp = customfunction.f(nums[mid],x)
            if temp == z:
                return nums[mid]
            elif z < temp:
                r = mid
            else:
                l = mid + 1
        return -1
