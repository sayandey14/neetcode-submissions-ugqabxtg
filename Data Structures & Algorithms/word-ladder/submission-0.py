class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        words = set(wordList)
        ret = 0

        queue = deque()
        queue.append(beginWord)

        while queue:
            ret+=1
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return ret
                for j in range(len(cur)):
                    for c in range(97,123):
                        if chr(c) == cur[j]:
                            continue
                        neighbor = cur[:j] + chr(c) + cur[j+1:]
                        if neighbor in words:
                            queue.append(neighbor)
                            words.remove(neighbor)
        return 0

        
