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
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if head == None:
			return None
		if head.next == None:
			return head

		length = 1
		prev, prevTail = None, head
		while prevTail.next != None:
			length += 1
			prevTail = prevTail.next
		prevTail.next = head

		ptr = head
		k %= length
		for i in range(length - k - 1):
			ptr = ptr.next
		newHead = ptr.next
		ptr.next = None
		return newHead

l = initListNode([1, 2, 3, 4, 5])
printListNode(Solution().rotateRight(l, 3))