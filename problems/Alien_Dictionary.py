class Solution:
    def alienOrder(self, words: list[str]) -> str:
        ans = ''
        adj = { c: set() for word in words for c in word}

        for i in range(len(words)-1):#check each adjacent pairs since words are sorted lexicographically
            wa,wb = words[i], words[i+1]
            minlen = min(len(wa), len(wb))
            if len(wa) > len(wb) and wa[:minlen] == wb[:minlen]:
                return ans
            for j in range(minlen):
                if wa[j] != wb[j]:
                    adj[wa[j]].add(wb[j])
                    break
        visit = {} #False chracter has been visited, True=current path
        ans = []
        def dfs(c):
            nonlocal visit
            if c in visit:
                return visit[c]
            visit[c] = True
            
            for nxt in adj[c]:
                if dfs(nxt):
                    return True

            visit[c] = False
            ans.append(c)
        for c in adj:
            if dfs(c):
                return ''
            
        ans.reverse()
        return ''.join(ans)




print(Solution().alienOrder( ["wrt","wrf","er","ett","rftt"] ) )