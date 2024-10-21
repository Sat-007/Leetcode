class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_counts = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomains = domain.split('.')
            #print(subdomains)
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain not in visit_counts:
                    visit_counts[subdomain] = 0
                visit_counts[subdomain] += count
                
        res = [f"{count} {subdomain}" for subdomain, count in visit_counts.items()]
        return res
                    