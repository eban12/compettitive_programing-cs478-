class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 1
        totalSize = 0
        for i in S:
            iSize = widths[ord(i) - ord('a')]
            if 100 - totalSize < iSize:
                totalSize = iSize
                lines += 1
            else:
                totalSize += iSize
        
        return [lines, totalSize]
