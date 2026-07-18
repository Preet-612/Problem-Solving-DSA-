class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        d = {}
        for i in range(26):
            d[order[i]] = i
        
        for i in range(n-1):
            s1 = words[i]
            s2 = words[i+1]

            if len(s1) > len(s2) and s1.startswith(s2):
                return False

            for u,v in zip(s1,s2):
                
                if u != v:
                    if d[u] > d[v]:
                        return False
                    break
        return True
                    
                    



            
