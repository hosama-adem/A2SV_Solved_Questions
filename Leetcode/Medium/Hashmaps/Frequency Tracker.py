class FrequencyTracker:

    def __init__(self):
        self.dict = defaultdict(int)
        self.freq = defaultdict(int)        

    def add(self, number: int) -> None:
        self.dict[number] += 1
        f = self.dict[number]
        self.freq[f] += 1
        self.freq[f-1] -=1

    def deleteOne(self, number: int) -> None:
        if self.dict[number] > 0:
            old_f = self.dict[number]
            self.freq[old_f] -= 1
            self.dict[number] -= 1
            new_f = self.dict[number]
            if new_f > 0:
                self.freq[new_f] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
