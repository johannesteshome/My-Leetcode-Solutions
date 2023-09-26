class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            pos = ord(char) - 97
            if not curr.children[pos]:
                curr.children[pos] = TrieNode()
            curr = curr.children[pos]
        curr.isEndOfWord += 1
    
    def checkLength(self, word: str, dic: dict) -> int:
        curr = self.root
        count = 0

        queue = deque([(curr, 0)])

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                currTrie = curr[0]
                currIndex = curr[1]

                count += currTrie.isEndOfWord

                for i in range(26):
                    if currTrie.children[i]:
                        # print(i)
                        index = bisect_left(dic[i], currIndex)
                        if index < len(dic[i]):
                            queue.append((currTrie.children[i], dic[i][index]+1)) 

        return count

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        obj = Trie()

        for word in words:
            obj.insert(word)
        
        dic = defaultdict(list)

        for i in range(len(s)):
            dic[ord(s[i])-97].append(i)
        print(dic)
        
        return obj.checkLength(s,dic)

        