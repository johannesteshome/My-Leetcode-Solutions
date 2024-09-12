class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        for s in words:
            found = True
            for i in range(len(s)):
                if s[i] not in allowed:
                    found = False
                    break
            if found:
                answer += 1
        
        return answer