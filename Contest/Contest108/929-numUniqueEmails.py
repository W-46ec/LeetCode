class Solution:
	def numUniqueEmails(self, emails):
		"""
		:type emails: List[str]
		:rtype: int
		"""
		emailLib = set()
		for e in emails:
			seperated = e.split('@')
			seperated[0] = seperated[0].replace('.', '')
			emailLib.add(seperated[0].split('+')[0] + seperated[1])
		return len(emailLib)

print(Solution().numUniqueEmails([
	"test.email+alex@leetcode.com", 
	"test.e.mail+bob.cathy@leetcode.com", 
	"testemail+david@lee.tcode.com"]
))