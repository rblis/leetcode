def solution(word):
    dic = [-1]*26
    for num, char in enumerate(word):
        nchar = ord(char)-97
        dic[nchar] =  num if dic[nchar] == -1 else abs(num)*-1 - 10        
    mins = 999999999
    for val in dic:
        if val > -1 and val < mins:
            mins = val
    return -1 if mins == 999999999 else mins

print(solution("leetcode"))