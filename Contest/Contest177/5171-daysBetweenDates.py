
from datetime import date

class Solution:
	def daysBetweenDates(self, date1: str, date2: str) -> int:
		year1, month1, day1 = [int(i) for i in date1.split('-')]
		year2, month2, day2 = [int(i) for i in date2.split('-')]
		return abs((date(year1, month1, day1) - date(year2, month2, day2)).days)


print(Solution().daysBetweenDates(date1 = "1970-01-01", date2 = "1971-01-01"))
print(Solution().daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))
print(Solution().daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))
