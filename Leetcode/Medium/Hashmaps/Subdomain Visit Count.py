class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        import collections
        counts = defaultdict(int)
        #i use from collection module because it safe for counting 
        result = []

        for i in cpdomains:
            num,domain = i.split()
            num = int(num)
            fra = domain.split(".")
            for j in range(len(fra)):
                key = ".".join(fra[j:])
                counts[key] +=num
        
        for key,values in counts.items():
            d=f"{values} {key}"
            result.append(d)

        return result
