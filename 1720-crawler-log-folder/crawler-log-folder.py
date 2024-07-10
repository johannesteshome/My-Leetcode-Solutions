class Solution:
    def minOperations(self, logs: List[str]) -> int:
        history = []
        for log in logs:
            action = log[:-1]

            if action != ".." and action != '.':
                history.append(action)
            elif action == "..":
                if history:
                    history.pop()
        
        return len(history)