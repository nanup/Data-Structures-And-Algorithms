class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        dec = 10
        rev_num = 0
        upper_limit = 2 ** 31

        while num > 0:
            last_digit = num % dec

            if upper_limit - last_digit < rev_num * dec:
                return 0

            rev_num = rev_num * 10 + last_digit
            num //= dec

        if x < 0:
          rev_num *= -1

        return rev_num