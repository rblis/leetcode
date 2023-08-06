# def solution(source):
#     ans = source[0]
#     tot = 0
#     cur = 0
#     cur_char = source[0]
#     for c in source:
#         if c != cur_char:
#             if cur > tot:
#                 tot = cur
#                 ans = cur_char
#             cur = 1
#             cur_char = c
#         else:
#             cur += 1
#     return ans+str(tot)

# print(solution('bbacccdbbab'))


# def solution(words):
#     ans = 0
#     for i in range(len(words)):
#         for j in range(i+1, len(words)):
#             a,b = words[i], words[j]
#             if len(a) > len(b):
#                 if a[len(a)-len(b):] == b:
#                     ans += 1
#             elif len(a) < len(b):
#                 if b[len(b)-len(a):] == a:
#                     ans += 1
#             else:
#                 if a == b:
#                     ans+= 1
#     return ans

def solution(text, limit):
    ans = []
    tot = 1
    lim = limit - 5
    pgs = 10
    cur = 0
    while True:
        if len(text)//lim < pgs:
            tot = len(text)//lim + 1
            break
        else:
            pgs *= 10
            lim += 1
    
    for i in range(tot):
        row = text[cur:cur+lim] + '<' + str(i+1) + '/' + str(tot) +'>'
        if text[cur:cur+lim] == '': return []
        ans.append(row)
        cur += lim

    return ans

print(solution('Very long message! More than 10 messages needed.', 10))

'''
Imagine that you are given some text that a user would like to send as a sequence of SMS messages. However, there is a limit specifying the maximum number of characters a single message can contain. Your task is to split all characters of text into the minimum number of SMS messages possible.

Each message must contain a part of the text, followed by the suffix <X/Y>, where Y is the total number of messages and X is the number of the current message (starting from 1). The suffix is considered to be a part of the message, so the total length of each message includes the length of the suffix. Only the last message in the sequence can be shorter than limit characters.

Iterate over all numbers of messages Y starting from 1. Remember to split text into as few SMS messages as possible. Return an array containing the sequence of SMS messages corresponding to this split. If it's not possible to split the text into different messages based on the limit, return an empty array.

For text = "Hello, world!" and limit = 10, the output should be

solution(text, limit) = ["Hello<1/3>",
                         ", wor<2/3>",
                         "ld!<3/3>"]
'''