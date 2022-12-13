class Solution:
    def reverse(self, x: int) -> int:
        X = str(x)
        if X[0] == "-":
            reversed = "-" + X[1:][::-1]
        else:
            reversed = str(x)[::-1]
        if float(reversed) >= 2 ** 31 or float(reversed) < -2 ** 31:
            return 0
        return int(reversed)