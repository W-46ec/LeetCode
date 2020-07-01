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
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if len(lists) == 0:
			return lists
		L = []
		for l in lists:
			if len(L) == 0:
				while l != None:
					L.append(l.val)
					l = l.next
			else:
				index = 0
				while l != None:
					if index < len(L):
						if l.val <= L[index]:
							L.insert(index, l.val)
							l = l.next
						else:
							index += 1
					else:
						L.insert(index, l.val)
						index += 1
						l = l.next
		return L

l1 = initListNode([1, 2, 4])
l2 = initListNode([1, 3, 4])
l3 = initListNode([2, 5, 7, 9])
print(Solution().mergeKLists([l1, l2, l3]))