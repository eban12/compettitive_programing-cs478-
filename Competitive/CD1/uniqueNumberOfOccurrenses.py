class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            
        # print(count)
        
        vals = list(counts.values())
        val2 = set(vals)
        
        if len(vals) != len(val2):
            return False
            
        return True
