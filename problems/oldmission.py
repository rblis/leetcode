# def solution(A: list[int]):
#     # write your code in Python 3.6
#     ans = 0
#     def recurse(index, res):
#         nonlocal ans
#         if index >= len(A):
#             if len(res) > 0:
#                 tot = res[0]
#                 for i in range(1,len(res)):
#                     tot &= res[i]
#                 if tot > 0:
#                     ans = max(ans, len(res))
#             return
#         recurse(index+1, res + [A[index]])
#         recurse(index + 1, res)
#     recurse(0,[])
#     return ans



# print(solution([16]))
import math
def solution(N):
    # write your code in Python 3.6
    def at(num, n):
        return num //10**n % 10
    if N < 10:
        return N + 1
    for i in range(N+1, 1000000000):
        check = True
        for j in range(1, int(math.log10(i))+1):
            if at(i,j) == at(i,j-1):
                check = False
                break
        if check:
            return i
print(solution(3298))

ex = [] 
for i in range(0,10):
    ex.append(lambda: print(i))

for lam in ex:
    lam()