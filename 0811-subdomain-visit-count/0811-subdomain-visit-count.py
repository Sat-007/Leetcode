class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit = {}
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            count = int(cpdomain[0])
            subdomains = cpdomain[1].split('.')
            #print(count)
            #print(subdomain)
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                if subdomain not in visit:
                    visit[subdomain] = 0 
                visit[subdomain] += count
        res = [f"{count} {subdomain}" for subdomain, count in visit.items()]
        return res
                
                
        