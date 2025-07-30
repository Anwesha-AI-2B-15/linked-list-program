{
		class Node:
		    def __init__(self, data):   
		        self.data = data
		        self.next = None
	}	
class Solution:
    def insertInMiddle(self, head, x):
        new_node = Node(x)
        if not head:
            return new_node
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        slow.next, new_node.next = new_node, slow.next
        return head


