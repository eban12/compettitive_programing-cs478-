class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        points = 0
        while tokens:
            if tokens[0] <= P:
                P -= tokens[0]
                points += 1
                tokens.pop(0)
            elif points >= 1 and len(tokens) > 1:
                P += tokens.pop()
                points -= 1
            
            else:
                break
        return points
