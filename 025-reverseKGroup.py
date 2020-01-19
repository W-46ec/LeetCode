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
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		l = []
		p = head
		while p != None:
			l.append(p.val)
			p = p.next
		
		idx = 0

		while idx + k - 1 < len(l):
			for i in range(idx, (idx + idx + k) // 2):
				l[i], l[idx + k - 1 - (i - idx)] = l[idx + k - 1 - (i - idx)], l[i]
			idx += k

		return l

		
l = initListNode([1, 2, 3, 4, 5])
print(Solution().reverseKGroup(l, 2))