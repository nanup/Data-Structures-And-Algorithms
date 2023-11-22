class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        start = 0
        swaps = 0
        k = k % len(nums)

        while swaps < len(nums):
            current = start
            prev_num = nums[current]

            while True:
                next = (current + k) % len(nums)
                nums[next], prev_num = prev_num, nums[next]
                current = next
                swaps += 1

                if current == start:
                    break

            start += 1
