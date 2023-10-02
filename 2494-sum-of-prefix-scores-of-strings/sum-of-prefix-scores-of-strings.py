class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = False

        self.count = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        def insert(word, again = False):
            curr = root
            for char in word:
                pos = ord(char) - 97
                if not curr.children[pos]:
                    curr.children[pos] = TrieNode()
                if curr.children[pos] and again:
                    curr.count += 1
                curr = curr.children[pos]
            if again:
                curr.count += 1
            curr.isEndOfWord = True
        
        def show():
            queue = deque([root])
            while queue:
                for _ in range(len(queue)):
                    currs  = queue.popleft()
                    for i in range(len(currs.children)):
                        if currs.children[i]:
                            print(chr(i+97), currs.children[i].isEndOfWord, currs.children[i].count)
                            queue.append(currs.children[i])
        visited = set()
        for word in words:
            if word in visited:
                insert(word, True)
            else:
                visited.add(word)
                insert(word)
        
        # show()

        def dfs(curr):
            found = False
            n = 0

            for i in range(26):
                
                if curr.children[i]:
                    found = True
                    n += dfs(curr.children[i])

            if not found:
                # print(curr.count, "last")
                curr.count += 1
                return 1
            
            if curr.isEndOfWord:
                curr.count += n+1
                return n+1
            else:
                curr.count += n
                return n
            # print(curr.count)
            
            # return n
        
        dfs(root)
        # print(dic)
        dic = {}
        # show()

        def dfsAnswer(curr, char, length):
            # print(length)

            for i in range(26):
                if curr.children[i]:
                    dfsAnswer(curr.children[i], char+chr(i+97), length+curr.children[i].count)
            
            if curr.isEndOfWord:
                dic[char] = length
        
        dfsAnswer(root, "", 0)
        answer = []
        # print(dic)
        for word in words:
            answer.append(dic[word])
        return answer

        