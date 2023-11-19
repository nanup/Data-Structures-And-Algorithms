class Solution:
    def check(self, nums: List[int]) -> bool:
        possibly_rotated = False

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if not possibly_rotated:
                    possibly_rotated = True
                else:
                    return False

        if possibly_rotated:
            if nums[-1] > nums[0]:
                return False

        return True
