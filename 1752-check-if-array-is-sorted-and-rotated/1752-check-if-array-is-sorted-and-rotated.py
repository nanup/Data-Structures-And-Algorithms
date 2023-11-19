class Solution:
    def check(self, nums: List[int]) -> bool:
        is_rotated = False
        
        for i in range(len(nums)):
          if nums[i] > nums[(i+1) % len(nums)]:
            if not is_rotated:
              is_rotated = True
            else:
              return False

        return True
