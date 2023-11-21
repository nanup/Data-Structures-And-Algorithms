class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        swap_count = 0
        start_index = 0

        while swap_count < n:
            current_index = start_index
            prev = nums[start_index]

            while True:
                next_index = (current_index+k) % n
                nums[next_index], prev = prev, nums[next_index]
                current_index = next_index
                swap_count += 1

                if start_index == current_index:
                    break

            start_index += 1

        return start_index
