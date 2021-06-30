class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        times = collections.Counter()
        # ["9001 discuss.leetcode.com"]
        for domain in cpdomains:
            # count = 9001, domain = discuss.leetcode.com
            count, domain = domain.split()
            count = int(count)
            # fragments = ["discuss","leetcode","com"]
            fragments=domain.split('.')
            for frag in range(len(fragments)):
                times[".".join(fragments[frag:])] += count

        return ["{} {}".format(count, domain) for domain, count in times.items()]
