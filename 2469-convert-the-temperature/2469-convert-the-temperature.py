class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        c = celsius
        f = (c * 1.80) + 32
        k = c + 273.15

        return [k,f] 