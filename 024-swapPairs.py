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
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None:
			return head
		p1 = head
		h = None
		isFirst = True
		while p1 != None:
			t = p1
			p1 = p1.next
			if p1 == None:
				break
			t.next = p1.next
			p1.next = t
			if isFirst:
				head = p1
				isFirst = False
			else:
				h.next = p1
			p1 = p1.next.next
			h = t
		return head

l = initListNode([1, 2, 3, 4, 5])
printListNode(Solution().swapPairs(l))