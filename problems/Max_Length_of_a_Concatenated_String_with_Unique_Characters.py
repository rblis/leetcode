class Solution:
    def maxLength(self, arr: list[str]) -> int:
        ans = 0
        def dfs(i, track):
            nonlocal ans
            if i >= len(arr):
                ans = max(ans, len(track))
                return
            check = True
            cur =set()
            for c in arr[i]:
                if c in track or c in cur:
                    check = False
                    break
                cur.add(c)
            if check: #include the character
                for c in arr[i]:
                    track.add(c)
                dfs(i+1, track)
                for c in arr[i]:
                    track.remove(c)
            dfs(i+1, track)#do no include the character
        for i in range(len(arr)):
            dfs(i,set())
        return ans

print(Solution().maxLength(["a", "abc", "d", "de", "def"]))
        