'''

def Solution(strs: [str]):
    maps = {}
    for word in strs:                
        sorte = "".join(sorted(word))
        if sorte not in maps.keys():
            maps[sorte] = [word]
        else:
            maps[sorte].append(word)        
    return maps.values()


print(Solution(["eat","tea","tan","ate","nat","bat"]))



Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


def Solution(strs):
    result = []
    rindx = 0
    for i in range(len(strs)):
        if strs[i] != "000":
            result.append([strs[i]]) 
            match = sorted(strs[i])             
            for j in range(i+1, len(strs)):
                if strs[j] != "000" and len(strs[i]) == len(strs[j]) and match == sorted(strs[j]):
                    result[rindx].append(strs[j])
                    strs[j] = "000"
            rindx += 1
            strs[i] = "000"
    return result
'''

strs = ["eat","tea","tan","ate","nat","bat"]
hamp = {}
for s in strs:
    ss = ''.join(sorted(s))
    if ss in hamp:
        hamp[ss].append(s)
    else:
        hamp[ss] = [s]
ans = [x for x in hamp.values()]
print(ans)