# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        path = head
        count = 0
        answer = []

        while path:
            count += 1
            path = path.next
        
        divs = count // k
        adds = count % k
        print(count, divs, adds)

        path = head

        if divs == 0:
            # print("here")
            while path:
                answer.append(path)
                temp = path.next
                path.next = None
                path = temp
            
            for _ in range(k - adds):
                answer.append(None)
        else:
            n = 0
            h1 = path

            while path:
                n += 1

                if n == divs and adds != 0:
                    print("here")
                    n = 0
                    adds -= 1
                    path = path.next
                    temp = path.next
                    path.next = None
                    path = temp
                    answer.append(h1)
                    h1 = path
                elif n == divs and adds == 0:
                    n = 0
                    temp = path.next
                    path.next = None
                    path = temp
                    answer.append(h1)
                    h1 = path
                else:
                    path = path.next



        return answer
        