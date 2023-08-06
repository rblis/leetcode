'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds, dt = {}, {}
        for c in t:
            dt[c] = dt.get(c, 0) + 1
        def check():
            nonlocal ds, dt
            for key in dt.keys():
                if key not in ds or dt[key] > ds[key]: return False
            return True
        lo, hi = 0, 0
        low, high = -1, -1
        while hi < len(s):
            c = s[hi]
            ds[c] = ds.get(c, 0) + 1
            if check():
                if low == high == -1 or hi-lo < high-low:
                    low = lo
                    high = hi
                while lo < hi:
                    cc = s[lo]
                    ds[cc] -= 1
                    lo += 1
                    if ds[cc] <= 0:
                        ds.pop(cc)
                    if not check():
                        break
                    if hi-lo < high-low:
                        low = lo
                        high = hi
            hi += 1
        return s[low:high+1] if not (low == high == -1) else ""


sol = Solution()
print(sol.minWindow('ADOBECODEBANC', 'ABC'))


# def check(win, dic):
#     perf = True
#     for key in dic:
#         if key not in win or (win[key] < dic[key] and win[key] != 0):
#             return [False, perf]
#         if win[key] > dic[key]:
#             perf = False
#     return [True, perf]

# def minWindow(s: str, t: str):
#     start, end = 0, 0
#     window, dicT = {}, {}
#     count = 0
#     minwin = 100000
#     result = ""
#     for c in t:
#         count += 1
#         if c in dicT:
#             dicT[c] += 1
#         else:
#             dicT[c] = 1
#     wincnt = 0
#     win = 0
#     for k in range(0, len(t)):
#         if len(s) < len(t):
#             return ""
#         wincnt += 1
#         if s[k] in dicT:
#             win+= 1
#         if s[k] in window:
#             window[s[k]] += 1
#         else:
#             window[s[k]] = 1
#         start += 1
#     chk = check(window, dicT)
#     if chk[0]:
#         if len(s) == len(t):
#             return s
#         elif chk[1]:
#             return s[end:start]
#     while start < len(s):
#         ss = s[start]
#         ee = s[end]
#         if s[start] in dicT:
#             win+= 1
#         if s[start] in window:
#             window[s[start]] += 1
#         else:
#             window[s[start]] = 1
#         wincnt += 1
#         if win >= count and len(window.items()) >= len(dicT.items()):
#             while start - end >= len(t)-1:
                
#                 if check(window, dicT)[0] and start-end < minwin:
                    
#                     result = ""
#                     if s[start] in dicT:
#                         minwin = start - end + 1
#                         for k in range(end, start + 1):
#                             result += s[k]
#                     else:
#                         minwin = start - end
#                         for k in range(end, start):
#                             result += s[k]
#                 if s[end] in dicT:
#                     if window[s[end]] > dicT[s[end]]:
#                         win -= 1
#                         window[s[end]] -= 1
#                         end +=1
#                         wincnt -= 1
#                     else:
#                         break                    
#                 else:
#                     window[s[end]] -= 1
#                     end +=1
#                     wincnt -= 1                
#                 if win < count:
#                     break
#         start += 1
        
#     return result        

# "ABXABXCCXAXBC"

# print(minWindow("aaabbaaba", "abbb"))
# "aaabbaaba"
# "abbb"
