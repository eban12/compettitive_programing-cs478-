class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookUp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        trans = set()
        for word in words:
            temp = ""
            for char in word:
                temp += lookUp[ord(char) - ord('a')]
                
            trans.add(temp)
        
        return len(trans)
