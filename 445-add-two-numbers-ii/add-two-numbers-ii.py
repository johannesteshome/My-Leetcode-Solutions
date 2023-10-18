# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        print(stack1, stack2)
        curr = 0
        Next = None
        while stack1 and stack2:
            num1 = stack1.pop()
            num2 = stack2.pop()

            if curr+num1 + num2 < 10:
                newNode = ListNode(curr+num1+num2)
                curr = 0
                newNode.next = Next
            else:
                newNode = ListNode((curr+num1+num2)%10)
                curr = (curr+num1+num2) // 10
                newNode.next = Next
            
            Next = newNode
        
        if stack1:
            while stack1:
                num1 = stack1.pop()
                if curr+num1 < 10:
                    newNode = ListNode(curr+num1)
                    curr = 0
                    newNode.next = Next
                else:
                    newNode = ListNode((curr+num1)%10)
                    curr = (curr+num1) // 10
                    newNode.next = Next
                
                Next = newNode
        
        if stack2:
            while stack2:
                num1 = stack2.pop()
                if curr+num1 < 10:
                    newNode = ListNode(curr+num1)
                    curr = 0
                    newNode.next = Next
                else:
                    newNode = ListNode((curr+num1)%10)
                    curr = (curr+num1) // 10
                    newNode.next = Next
                
                Next = newNode
        
        if curr != 0:
            newNode = ListNode(curr)
            newNode.next = Next
            Next = newNode
        
        return Next
            