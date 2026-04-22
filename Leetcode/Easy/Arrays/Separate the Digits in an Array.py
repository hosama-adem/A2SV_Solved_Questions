class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        all =[str(i) for i in nums]
        all = "".join(all)
        digits = [int(num) for num in all]
        return digits
