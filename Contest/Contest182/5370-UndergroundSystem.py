
class UndergroundSystem:

    def __init__(self):
        self.ids = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t1 = self.ids[id]
        difference = t - t1
        if (startStation, stationName) not in self.times:
            self.times[(startStation, stationName)] = (difference, 1)
        else:
            totalTime, num = self.times[(startStation, stationName)]
            self.times[(startStation, stationName)] = (totalTime + difference, num + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, num = self.times[(startStation, endStation)]
        return totalTime / num
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))    # return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       # return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       # return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       # return 12.0
