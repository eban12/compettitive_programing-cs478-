class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dictionary = {}
        def helper(idx,t):
            if not (idx,t) in dictionary:
                if idx == len(nums):
                    if S == t:
                        return 1
                    return 0
                else:
                    count = 0
                    count += helper(idx+1,t + nums[idx])
                    count += helper(idx+1,t-nums[idx])
                    dictionary[(idx,t)] = count
            return dictionary[(idx,t)]
            
        return helper(0,0)
     
