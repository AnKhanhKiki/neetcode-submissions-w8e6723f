class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            s = sorted(i)
            s = ''.join(s)
            ans[s].append(i)
        return list(ans.values())

