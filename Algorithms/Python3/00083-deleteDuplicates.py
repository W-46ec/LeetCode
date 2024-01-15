# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def initListNode(l):
	if len(l) == 0:
		return ListNode(None)
	elif len(l) == 1:
		return ListNode(l[0])
	else:
		lNode = ListNode(l[0])
		head = lNode
		for i in range(1, len(l)):
			lNode.next = ListNode(l[i])
			lNode = lNode.next
		return head

# Test
def printListNode(l):
	if l != None:
		while l != None:
			print(l.val, end = ' ')
			l = l.next
		print('\n')

class Solution:
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None:
			return None
		p = head
		while p.next != None:
			if p.val == p.next.val:
				p.next = p.next.next
			else:
				p = p.next
		return head


l = initListNode([1, 1, 2, 2, 2, 4, 5])
printListNode(Solution().deleteDuplicates(l))