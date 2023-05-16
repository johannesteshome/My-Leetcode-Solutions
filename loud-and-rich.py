class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # initialize the graph and answer array
        adjList = defaultdict(list)
        answer = [None for i in range(len(quiet))]

        # write the graph in way of increasing richness i.e. as we go deep we go to the richer nodes
        for rich, poor in richer:
            adjList[poor].append(rich)
        
        # the dfs
        def dfs(node):
            # no need to check for nodes that have already found least quiet values
            if answer[node] != None:
                return
            # we initialize the poorer node as the least quiet and update it as we go deep into the richer nodes
            leastQuiet = node

            if node in adjList:
                for children in adjList[node]:
                    # recursively the DFS is called to go the richest node and find its quiet value since it may be the answer for the poorer nodes that precede them
                    dfs(children)
                    # the leastQUiet is updated based on whether there is a richer node that has least quiet value than itself depper in the graph
                    leastQuiet = min(leastQuiet, answer[children], key=lambda x: quiet[x])
            
            answer[node] = leastQuiet
        
        for i in range(len(answer)):
            if answer[i] == None:
                dfs(i)

        
        
        return answer