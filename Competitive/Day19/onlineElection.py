class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.queryArr = []
        self.times = times
        
        dictionary = {}
        curMax = persons[0]
        for person in persons:
            if person in dictionary:
                dictionary[person] += 1
            else:
                dictionary[person] = 1
            
            if dictionary[person] >= dictionary[curMax]:
                curMax = person
            self.queryArr.append(curMax)
    

    def q(self, t: int) -> int:
        if t > self.times[-1]:
            return self.queryArr[-1]
        
        left = 0
        right = len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == t:
                return self.queryArr[mid]
            elif mid > 0 and self.times[mid] > t and self.times[mid - 1] <= t:
                return self.queryArr[mid-1]
            elif mid > 0 and self.times[mid] > t and self.times[mid - 1] > t:
                right = mid - 1
            elif mid + 1 < len(self.times) and self.times[mid] < t and self.times[mid + 1] > t:
                return self.queryArr[mid]
            else:
                left = mid + 1
        
            
            
            
            
            
            
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
