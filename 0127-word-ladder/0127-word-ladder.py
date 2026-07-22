class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        setword = set(wordList)
        if endWord not in setword:
            return 0
        
        q = deque([(beginWord,1)])

        while q:

            word, level = q.popleft()

            if word == endWord:
                return level
            
            word = list(word)
            for i in range(len(word)):

                original = word[i]

                for ch in 'abcdefghijklmnopqrstuvwxyz':

                    word[i] = ch
                    newword = "".join(word)

                    if newword in setword:
                        q.append((newword,level+1))
                        setword.remove(newword)
            
                word[i] = original
        return 0






