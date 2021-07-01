class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 只有当数字重复出现，才在计数它出现次数的同时，记录它出现的位置
        # 用哈希表实现，将对应数字映射到[出现次数, 出生位置，最后以此出现的位置]
        info = dict()

        for i, num in enumerate(nums):
            if num in info:
                info[num][0] += 1
                info[num][2] = i
            else:
                info[num] = [1, i, i]
        
        # 开始比大小，比较众数出现次数的同时比较连续数组长度
        maxDeg = minLen = 0
        for cnt, leftPos, rightPos in info.values():
            if cnt > maxDeg:
                maxDeg = cnt
                minLen = rightPos - leftPos + 1
            elif cnt == maxDeg:
                # 如果有多个相同度的众数，比较它们连续数组的长度，取较小
                if minLen > (span := rightPos - leftPos + 1):
                    minLen = span
        
        return minLen

# 时间复杂度：遍历数组生成哈希表+遍历哈希表找最短连续数组长度=O(2n)=O(n)
# 空间复杂度：O(n); 最坏情况下，数组中每个数都不一样，哈希表长度与原数组相同
