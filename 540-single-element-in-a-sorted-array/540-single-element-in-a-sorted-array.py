class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    end = mid - 1
                elif nums[mid] == nums[mid + 1]:
                    start = mid + 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    end = mid - 1
                else:
                    return nums[mid]
                
        return nums[start]
                    