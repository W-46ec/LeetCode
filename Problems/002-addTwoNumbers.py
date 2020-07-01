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

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		list1 = []
		list2 = []
		longestLen = 0

		if l1 == None and l2 == None:
			return []
		elif l1 == None:
			return l2
		elif l2 == None:
			return l1

		while l1 != None:
			list1.append(l1.val)
			l1 = l1.next
		while l2 != None:
			list2.append(l2.val)
			l2 = l2.next

		if len(list1) > len(list2):
			longestLen = len(list1)
		else:
			longestLen = len(list2)
			l = list2
			list2 = list1
			list1 = l

		carry = 0
		for i in range(0, longestLen):
			if i < len(list2):
				digit = (list1[i] + list2[i] + carry) % 10
				carry = int((list1[i] + list2[i] + carry) / 10)
				list1[i] = digit
			else:
				digit = (list1[i] + carry) % 10
				carry = int((list1[i] + carry) / 10)
				list1[i] = digit
		if carry == 1:
			list1.append(carry)
		return list1

l1 = initListNode([9, 9, 9])
l2 = initListNode([1])
print(Solution().addTwoNumbers(l1, l2))