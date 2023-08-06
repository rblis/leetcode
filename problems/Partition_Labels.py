'''
A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible
 so that each letter appears in at most one part, 
 and return a list of integers representing the size of these parts.


 Solution: scan through list and keep an up to date index of the last 
 position of a particular character

 Then iterate over again and maintain a sliding window of indexes. Increase 
 the end of the window if any new character inside the current window has an 
 index larger than the current end index for the window. Append to answer whenevver the current index matches the end index and reset window sliders.
'''

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ans = []
        dic = {}
        for i,c in enumerate(s):
            dic[c] = i
        start = 0
        end = 0
        for i,c in enumerate(s):
            if dic[c] > start:
                start = dic[c]
            if start == i:
                ans.append(start-end+1)
                end = start + 1
        return ans


print(Solution().partitionLabels("caedbdedda"))
























# def partitionLabels(S: str) -> []:
#     dic, partitions, count = {}, [], 0
#     for index, char in enumerate(S):
#         if char in dic:
#             dic[char] =  index               
#         else:
#             dic[char] = -1    
#     endex = dic[S[0]]    
#     for index, char in enumerate(S):
#         if dic[char] == -1 and endex < index:
#             partitions.append(1)
#         else:
#             if index == endex:
#                 partitions.append(count+1)
#                 count = 0
#             elif dic[char] > endex:
#                 endex = dic[char]
#                 count += 1
#             else:
#                 count += 1
        
#     #print(partitions)        
#     return(partitions)