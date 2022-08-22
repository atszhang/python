import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    def groupAnagrams2(self, strs):
        ans = collections.defaultdict(list)

        for str in strs:
            strKey = [0] * 26
            for i in range(len(str)):
                strKey[ord(str[i]) - ord('a')] = strKey[ord(str[i]) - ord('a')] + 1
            ans[tuple(strKey)].append(str)

        return ans.values()

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams( strs))