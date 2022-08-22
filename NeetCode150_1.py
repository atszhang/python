from typing import List
class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

nums = [1,2,3,4,5,6,7,8,12, 2,143]
xx = ContainsDuplicate()
print(xx.containsDuplicate(nums))

class ContainsDuplicate2:
    def containsDuplicate2(nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

nums2 = [1,2,3,4,5,6,7,8,12, 12]
yy = ContainsDuplicate()
print(yy.containsDuplicate(nums2))