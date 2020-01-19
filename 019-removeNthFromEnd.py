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
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		length = 0
		p = head
		while p != None:
			length += 1
			p = p.next
		if length == 2:
			if n == 1:
				head.next = None
				return head
			elif n == 2:
				head = head.next
				return head
		i = length - n
		count = 0
		p = head
		while count < i - 1:
			p = p.next
			count += 1
		if count == 0:
			if i == 0:
				head = head.next
			elif i == 1:
				head.next = head.next.next
		else:
			p.next = p.next.next
		return head

		# if length == 1:
		# 	return None
		# if length == 2:
		# 	if n == 1:
		# 		head.next = None
		# 		return head
		# 	elif n == 2:
		# 		head = head.next
		# 		return head
		# count = 0
		# p = head
		# while count < length - n - 1:
		# 	p = p.next
		# 	count += 1
		# if count == 0:
		# 	head = head.next
		# elif count < length - 1:
		# 	p.next = p.next.next
		# return head

l1 = initListNode([1, 2, 4, 5, 7])
l2 = initListNode([1, 2, 3])
printListNode(Solution().removeNthFromEnd(l2, 1))