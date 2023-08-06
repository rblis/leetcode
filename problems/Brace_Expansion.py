'''
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

Example 1:
Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

Example 2:
Input: "abcd"
Output: ["abcd"]

Note:
1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
'''

class Solution:
    def expand(self, s: str) -> list[str]:
        ans = []
        def recurse(i,cur):
            if i >= len(s):
                ans.append(cur)
                return
            skip = i + 1
            if s[i] == '{':
                reps = []
                for j in range(i+1, len(s)):
                    if str.isalpha(s[j]):
                        reps.append(s[j])
                    elif s[j] == '}':
                        skip = j+1
                        break
                for c in reps:
                    recurse(skip, cur+c)
            else:
                recurse(skip, cur + s[i])
        recurse(0,'')
        return ans

print(Solution().expand('{b,c}{b,c}'))