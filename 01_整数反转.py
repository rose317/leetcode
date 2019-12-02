class Solution:
    def removeElement(self, nums, val):
        pre = 0
        las = len(nums) - 1
        while pre < las:
            if nums[pre] == val and nums[las] != val:
                nums[pre],nums[las] = nums[las], nums[pre]
                las -= 1
                pre += 1
            elif nums[pre] != val:
                pre += 1
            elif nums[las] == val:
                las -= 1

        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                res += 1
            else:
                return res


        print(nums)



li = Solution()
li.removeElement([0,1,2,2,3,0,4,2,2],2)