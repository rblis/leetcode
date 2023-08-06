










































# def solution(preferences):
#     dic = {}
#     for pref in preferences:
#         for i, p in enumerate(pref):
#             if p in dic:
#                 dic[p] += 1*(pow((len(pref)-i),10))
#             else:
#                 dic[p] = 1*(pow((len(pref)-i),10))
#     fav = 0.0
#     res = -1
#     for key in dic.keys():
#         if fav == 0.0:
#             fav = dic[key]
#             res = key
#         else:
#             if dic[key] > fav:
#                 fav = dic[key]
#                 res = key
#             elif dic[key] == fav:
#                 res = - 1
#     return res

# pp = [[3,5,2,6,10,1,7,8,4,9],  [8,7,2,4,10,1,5,3,6,9], [7,3,2,10,6,4,1,9,5,8]]
# print(solution(pp))









































# import heapq
# def solution(s):
#     pals = []
#     while True:
#         for i in range(0, len(s)):
#             for j in range(i+1,len(s)):
#                 pre = s[i:j+1]
#                 #print(pre)
#                 pal = ''.join(reversed(pre))
#                 if pal == pre:
#                     heapq.heappush(pals, (-len(pre), i, j))
#         long = heapq.heappop(pals) if len(pals) > 0 else [0]
#         if -long[0] > 1:
#             s = s[0:long[1]] + s[long[2]+1:]
#             pals = []
#             #print(s)
#         else:
#             break
#     return s

# solution('aaabba')












# def solution(s):
#     count = 0
#     for i in range(1, len(s)-1):
#         for j in range(i+1,len(s)):
#             a,b,c = s[:i], s[i:j], s[j:]
#             ab,bc, ca = s[:j], s[i:], s[j:] + s[:i]
#             print(a,b,c)
#             #print(ab,bc,ca)
#             if ab != bc and ab != ca and bc != ca:
#                 count += 1
#     return count
# solution("xzxzx")
# def solution(queryType, query):
#     dic = {}
#     ans = 0
#     shift = 0
#     for i,que in enumerate(queryType):
#         if que == 'insert':
#             dic[query[i][0]-shift] = query[i][1]
#         if que == "get":
#              ans += dic[query[i][0]-shift] if query[i][0]-shift in dic else 0
#         if que == "addToKey":
#             shift += query[i][0]
#         if que == "addToValue":
#             for key in dic.keys():
#                 dic[key] += query[i][0]
#     return ans



# print(solution(["insert", "insert", "addToValue", "addToKey", "get"], [[1,2], [2,3], [2], [1], [3]]))













'''
def solution(a):
    for i in range(len(a)//2):
        x,b,c = a[i], a[-(i+1)], a[-(i)]
        if a[i] >= a[-(i+1)]:
            return False
        if a[i] <= a[-(i)]:
            return False
    if len(a) > 2 and len(a)%2 == 1 and a[len(a)//2] < a[len(a)//2+1]:
        return False 
    return True 

print(solution([-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]))


Each query is represented as a pair of indices (i, j). For each query, perform the following operations:

    Select the ith-smallest value among the black cells. In case of a tie, select the one with the lower row number. If there is still a tie, select the one with the lower column number;
    Select the jth-smallest white cell using the same process;
    Find the average value of these two cells;
        If the average value is a whole integer, replace both of the selected cells with the found average value;
        Otherwise, replace the cell of the greater value with the average rounded up to the nearest integer, and replace the cell of the smaller value with the average rounded down to the nearest integer.

Your task is to return the resulting matrix after processing all the queries.

Example

    For

    matrix = [[2, 0, 4],
              [2, 8, 5],
              [6, 0, 9],
              [2, 7, 10],
              [4, 3, 4]]

    and queries = [[0, 0], [1, 3]], the output should be

    solution(matrix, queries) = [[1, 2, 4],
                                          [2, 8, 5],
                                          [6, 0, 9],
                                          [2, 7, 10],
                                          [4, 3, 3]]



                                          Given an array of integers arr and a positive integer m, your task is to find the frequency of the most common element within each contiguous subarray of length m in arr.

Return an array of these highest frequencies among subarray elements, ordered by their corresponding subarray's starting index. You can look at the examples section for a better understanding.

Example

    For arr = [1, 2] and m = 2, the output should be solution(arr, m) = [1].

    example 1

    arr contains only one contiguous subarray of length m = 2 - arr[0..1] = [1, 2]. This subarray contains 2 most frequent elements - 1 and 2, both having a frequency of 1. So, the answer is [1].

    For arr = [1, 3, 2, 2, 3] and m = 4, the output should be solution(arr, m) = [2, 2].

    example 2

    arr contains two contiguous subarrays of length m = 4:
        arr[0..3] = [1, 3, 2, 2] contains only one most frequent element - 2, and its frequency is 2.
        arr[1..4] = [3, 2, 2, 3] contains two most frequent elements - 2 and 3, both of them have a frequency of 2.
        Putting the answers for both subarrays together, we obtain the array [2, 2]

    For arr = [2, 1, 2, 3, 3, 2, 2, 2, 2, 1] and m = 3, the output should be solution(arr, m) = [2, 1, 2, 2, 2, 3, 3, 2].

    example 3

    arr contains 8 contiguous subarrays of length m = 3:
        arr[0..2] = [2, 1, 2] contains only one most frequent element - 2, and its frequency is 2.
        arr[1..3] = [1, 2, 3] contains three most frequent elements - 1, 2, and 3. All of them have frequency 1.
        arr[2..4] = [2, 3, 3] contains only one most frequent element - 3, and its frequency is 2.
        arr[3..5] = [3, 3, 2] contains only one most frequent element - 3, and its frequency is 2.
        arr[4..6] = [3, 2, 2] contains only one most frequent element - 2, and its frequency is 2.
        arr[5..7] = [2, 2, 2] contains only one most frequent element - 2, and its frequency is 3.
        arr[6..8] = [2, 2, 2] contains only one most frequent element - 2, and its frequency is 3.
        arr[7..9] = [2, 2, 1] contains only one most frequent element - 1, and its frequency is 2.
        Putting the answers for both subarrays together, we obtain the array [2, 1, 2, 2, 2, 3, 3, 2].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer arr

    An array of integers.

    Guaranteed constraints:
    2 ≤ arr.length ≤ 105,
    -109 ≤ arr[i] ≤ 109.

    [input] integer m

    An integer representing the length of each subarray.

    Guaranteed constraints:
    2 ≤ m ≤ arr.length.

    [output] array.integer

    An array of the highest frequencies in each contiguous subarray of length m in arr.

def solution(arr, m):
    size = len(arr)
    most = 0
    nums = 0
    dic = {}
    ans = []
    for i in range(m):
        dic[arr[i]] = dic[arr[i]] + 1 if arr[i] in dic else 1
        if dic[arr[i]] > nums:
            most = arr[i]
            nums = dic[arr[i]]
    dic[arr[0]] -= 1
    if most == arr[0]:
        nums-=1
    ans.append(most)
    for i in range(1, size):
        last = i-m if i-m >= 0 else 0
        first = i+m if i+m < size else size-1
        dic[arr[first]] = dic[arr[first]] + 1 if arr[first] in dic else 1
        if dic[arr[i]] >= nums:
            if dic[arr[i]] == nums:
                if arr[i] < most:
                    most = arr[i]
            else:
                most = arr[i] 
            nums = dic[arr[i]]
        if most == arr[last]:
            nums -= 1
        dic[arr[last]] -= 1
        ans.append(most)
    return ans



print(solution([2, 1, 2, 3, 3, 2, 2, 2, 2, 1], 3))



You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

Example

    For

    a = [[3, 3, 4, 2],
         [4, 4],
         [4, 0, 3, 3],
         [2, 3],
         [3, 3, 3]]

    the output should be

    solution(a) = [[0, 4],
                     [1],
                     [2, 3]]

        mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
        mean(a[1]) = (4 + 4) / 2 = 4;
        mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
        mean(a[3]) = (2 + 3) / 2 = 2.5;
        mean(a[4]) = (3 + 3 + 3) / 3 = 3.

    There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:
        Arrays with indices 0 and 4 form a group with mean 3;
        Array with index 1 forms a group with mean 4;
        Arrays with indices 2 and 3 form a group with mean 2.5.

    Note that neither

    solution(a) = [[0, 4],
                     [2, 3],
                     [1]]

    nor

    solution(a) = [[0, 4],
                     [1],
                     [3, 2]]

    will be considered as a correct answer:
        In the first case, the minimal element in the array at index 2 is 1, and it is less then the minimal element in the array at index 1, which is 2.
        In the second case, the array at index 2 is not sorted in ascending order.

    For

    a = [[-5, 2, 3],
         [0, 0],
         [0],
         [-100, 100]]

    the output should be

    solution(a) = [[0, 1, 2, 3]]

    The mean values of all of the arrays are 0, so all of them are in the same group.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.integer a

    An array of arrays of integers.

    Guaranteed constraints:
    1 ≤ a.length ≤ 100,
    1 ≤ a[i].length ≤ 100,
    -100 ≤ a[i][j] ≤ 100.

    [output] array.array.integer

    An array of arrays, representing the groups of indices.

[Python 3] Syntax Tips

def solution(a):
    dic = {}
    for i, ar in enumerate(a):
        mean = 0
        for num in ar:
            mean += num
        mean = mean/len(ar)
        if mean in dic:
            dic[mean].append(i)
        else:
            dic[mean] = []
    sol = []
    for key in dic.keys():
        sol.append(dic[key])
    print(sol)
    sol.sort(key= lambda x: x)
solution([[1,2], [2,2]])

'''