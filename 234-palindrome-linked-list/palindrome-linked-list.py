# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left=ListNode(0, head)
        def recursiveFunc(head):
            if not head:
                return True
            right = recursiveFunc(head.next)
            self.left = self.left.next
            return right and self.left.val== head.val
        return recursiveFunc(head)        
        # stack =[]
        # curr = head
        # while curr:
        #     stack.append(curr.val)
        #     curr= curr.next
        # curr = head
        # while curr:
        #     if curr.val!= stack.pop():
        #         return False
        #     curr=curr.next
        # return True          
        