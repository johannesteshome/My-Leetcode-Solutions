class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        increasing = defaultdict(list)
        decreasing = defaultdict(list)

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    increasing[rating[i]].append(rating[j])
                elif rating[i] > rating[j]:
                    decreasing[rating[i]].append(rating[j])
        
        # print(increasing, "increasing")
        # print(decreasing, "decreasing")
        for k in increasing:
            for i in increasing[k]:
                if i in increasing:
                    ans += len(increasing[i])
        
        for k in decreasing:
            for i in decreasing[k]:
                if i in decreasing:
                    ans += len(decreasing[i])
        
        return ans