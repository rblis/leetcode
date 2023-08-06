class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) >  len(haystack): return -1
        da,db = {}, {}
        def check(i):
            for j in range(len(needle)):
                if needle[j] != haystack[i]: return False
                i += 1
            return True
        for i in range(len(needle)):
            da[needle[i]] = da.get(needle[i], 0) + 1
            db[haystack[i]] = db.get(haystack[i],0) + 1

        if da == db and check(0): return 0

        lo = 0
        for hi in range(len(needle), len(haystack)):
            db[haystack[hi]] = db.get(haystack[hi], 0) + 1
            db[haystack[lo]] -= 1
            if db[haystack[lo]] == 0: db.pop(haystack[lo])
            lo += 1
            if da == db and check(lo): return lo

        if da == db and check(lo): return lo
        return -1

print(Solution().strStr(haystack = "zadbutsad", needle = "sad"))