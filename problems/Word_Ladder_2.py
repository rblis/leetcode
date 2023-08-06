import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        else:
            if len(beginWord) == 1:
                return 2
        dic = collections.defaultdict(list)
        pats = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:            
            for i in range(len(word)):
                pattern = word[:i] + '#' + word[i+1:]
                dic[pattern].append(word)
                pats[word].append(pattern)
        wordList.pop()
        path = set(beginWord)
        que = collections.deque([beginWord])
        ans = 1
        while que:
            for i in range(len(que)):#this only pops the amt of elements from previous level
                word = que.popleft()
                if word == endWord:
                    return ans
                if word not in path:#prevent iterating back to previous level
                    for pattern in pats[word]:#all the patterns associated with the word
                        for adj_word in dic[pattern]:#all the words associated with pattern
                            if adj_word not in path:
                                que.append(adj_word)#append all the words that follow given pattern
                                path.add(word)
            ans += 1
        return 0

    #create dic and add paterns
    #do a bfs on patterns to find shortest path

print(Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))