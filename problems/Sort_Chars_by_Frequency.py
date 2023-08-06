'''
Given a string, sort it in decreasing order based on the frequency of characters.

'''
import heapq

def solution(word: str):
    alph = {}
    for let in word:
        if let not in alph:
            alph[let] = 1
        else:
            alph[let] += 1
    result = ""

    #slightly faster approach using a priority queue
    h = [0]*len(alph.keys())
    
    for k, key in enumerate(alph.keys()):
        h[k] = (-1*alph[key], key)
    heapq.heapify(h)
    for j in range(len(alph.keys())):
        key = heapq.heappop(h)
        for i in range(-1*key[0]):
            result += key[1]
    #slightly slower appraoch using NLogN Sort
    # for key in sorted(alph.items(), key = lambda x: x[1], reverse=True):
    #     for i in range(key[1]):
    #         result += key[0]
    return result

print(solution("tree"))        
