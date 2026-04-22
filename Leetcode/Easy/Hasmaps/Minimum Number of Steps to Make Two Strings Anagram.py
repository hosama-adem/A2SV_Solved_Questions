class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d=Counter(s)
        e=Counter(t)
        steps = 0
        for i in d:
            if i in t and d[i]>e[i]:
                steps += d[i]-e[i]
            if i not in t:
                steps += d[i]
        return steps
