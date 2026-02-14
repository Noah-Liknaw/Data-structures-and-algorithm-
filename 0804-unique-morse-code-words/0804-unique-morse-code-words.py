from collections import Counter
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = list(range(0,26))

        alphaMorse = dict(zip(alphabet,morse))
        lt = []
        for s in words:
            ts = ""
            for c in s:
                ts+=alphaMorse[ord(c)-97]
            lt.append(ts)
        ct = Counter(lt)
        count = 0
        for key,value in ct.items():
            count+=1
        
        return count

        
        
        print(ct)