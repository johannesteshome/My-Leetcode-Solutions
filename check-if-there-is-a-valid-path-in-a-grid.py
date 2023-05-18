class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        unionSet = {}
        size = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                unionSet[(i,j)] = (i,j)
                size[(i,j)] = 1

        direction = {
            'left': (0, -1),
            'right': (0, 1),
            'up': (-1, 0),
            'down': (1, 0)
        }

        allowed = {
            1: ['left', 'right'],
            2: ['down', 'up'],
            3: ['left', 'down'],
            4: ['down', 'right'],
            5: ['left', 'up'],
            6: ['up', 'right']
        }

        possibles = {
            (1, 'right'): set([1,3,5]),
            (1, 'left'): set([1,4,6]),
            (2,'up'): set([3,4,2]),
            (2, 'down'): set([5,6,2]),
            (3, 'left'): set([1,6,4]),
            (3, 'down'): set([6,2,5]),
            (4, 'down'): set([5,6,2]),
            (4, 'right'): set([5,1,3]),
            (5, 'left'): set([6,1,4]),
            (5, 'up'): set([3,2,4]),
            (6, 'up'): set([4,3,2]),
            (6, 'right'): set([5,1,3])
        }

        def representative(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = representative(member1)
            repMember2 = representative(member2)

            if repMember1 != repMember2:
                if size[repMember1] < size[repMember2]:
                    unionSet[repMember1] = repMember2
                    size[repMember2] += size[repMember1]
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                road = grid[i][j]
                for path in allowed[road]:
                    # print(direction[path][0])
                    nextPath = (i + direction[path][0], j + direction[path][1])
                    if 0 <= nextPath[0] < len(grid) and 0 <= nextPath[1] < len(grid[0]):
                        # print(nextPath, (i,j), path)
                        if grid[nextPath[0]][nextPath[1]] in possibles[(road, path)]:
                            # print(possibles[(road, path)])
                            union((i, j), nextPath)

        # print(unionSet, possibles[(1,'right')])

        return representative((0,0)) == representative((len(grid)-1, len(grid[0])-1))