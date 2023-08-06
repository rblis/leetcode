class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        def recurse(i):
            reps = ''
            k = ''
            while i < len(s):
                c = s[i]
                if str.isalpha(c):
                    reps += c
                    i+=1
                elif str.isdigit(c):
                    k+= c
                    i += 1
                elif c == '[':
                    ret = recurse(i+1)
                    res = ret[0]
                    i = ret[1]
                    for j in range(int(k)):
                        reps += res
                    k = ''
                    i += 1
                else:
                    return (reps, i)
            return (reps, i+1)
        index = 0
        while index < len(s):
            ret = recurse(index)
            ans += ret[0]
            index = ret[1]
            index += 1
        return ans

print(Solution().decodeString( "2[x2[b]cc2[d]]" ))
# print("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")


