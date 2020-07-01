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
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		l = []
		index = 0

		if l1 == None and l2 == None:
			return []
		elif l1 == None:
			return l2
		elif l2 == None:
			return l1

		while l1 != None:
			l.append(l1.val)
			l1 = l1.next
		while l2 != None:
			if index < len(l):
				if l2.val <= l[index]:
					l.insert(index, l2.val)
					l2 = l2.next
				else:
					index += 1
			else:
				l.insert(index, l2.val)
				index += 1
				l2 = l2.next
		return l


l1 = initListNode([1, 2, 4])
l2 = initListNode([1, 3, 4])
print(Solution().mergeTwoLists(l1, l2))