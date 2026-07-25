class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            nextLevel = defaultdict(list)

            # Remove current level words to avoid revisiting
            wordSet -= level

            for word in level:
                wordChars = list(word)

                for i in range(len(wordChars)):
                    original = wordChars[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        wordChars[i] = c
                        newWord = "".join(wordChars)

                        if newWord in wordSet:
                            nextLevel[newWord].append(word)

                            if newWord == endWord:
                                found = True

                    wordChars[i] = original

            level = set(nextLevel.keys())

            for word in nextLevel:
                parents[word].extend(nextLevel[word])

        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return ans