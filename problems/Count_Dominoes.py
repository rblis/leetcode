class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        doms = list(dominoes)
        count = len(dominoes)
        while count > 2:
            rights = []
            lefts = []
            for i in range(1,len(doms)-1):
                if doms[i] == '.' and doms[i-1] == 'R':
                    if doms[i+1] == 'L':
                        count -= 1
                    else:
                        rights.append(i)
                        count -=1 
                elif doms[i] == '.' and doms[i+1] == 'L':
                    if doms[i-1] == 'R':
                        count -= 1
                    else:
                        lefts.append(i)
                        count -= 1
                else:
                    count -= 1
            for i in rights:
                doms[i] = 'R'
            for i in lefts:
                doms[i] = 'L'
        if doms[1] == 'L':
            doms[0] = 'L'
        if doms[-2] == 'R':
            doms[-1] = 'R'
        return ''.join(doms)
print(Solution().pushDominoes(".L.R...LR..L.."))