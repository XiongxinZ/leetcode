from typing import Counter, List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            #初始化和为0的子数组个数为1，方便之后计数从头开始算起的子数组和
            sum_dict = Counter([0])
            count = sum = 0
            for x in nums:
                sum += x
                if sum - k in sum_dict:
                    # 求多少个s[j] = s[i] - k
                    count += sum_dict[sum - k]
                sum_dict[sum] += 1
            return count
        
        def horizontalSum(matrix: List[List[int]], target: int) -> int:
            # 先算出每一行子数组的元素和
            # 然后对于子数组的元素和集
            # 用找一维子数组对应和的方法统计相应个数
            row, col = len(matrix), len(matrix[0])
            countAll = 0
            # 拉出左边界框
            for i in range(col):
                # 起始化一个长度为行数的数组
                sub_total = [0] * row
                # 拉出右边界框
                for j in range(i, col):
                    for k in range(row):
                        # 更新每行的元素和
                        sub_total[k] += matrix[k][j]
                    countAll += subarraySum(sub_total, target)
        
            return countAll

        # 时间复杂度：O(n^2*m), m、n为矩阵的行数以及列数
        # 空间复杂度：O(m), m为矩阵的行数

        def verticalSum(matrix: List[List[int]], target: int) -> int:
            # 先算出每一列子数组的元素和
            # 然后对于子数组的元素和集
            # 用找一维子数组对应和的方法统计相应个数
            row, col = len(matrix), len(matrix[0])
            countAll = 0
            # 上边界
            for i in range(row):
                # 起始化一个长度为行数的数组
                sub_total = [0] * col
                # 下边界
                for j in range(i, row):
                    for k in range(col):
                        # 更新每列的元素和
                        sub_total[k] += matrix[j][k]
                    countAll += subarraySum(sub_total, target)
        
            return countAll
        
        # 时间复杂度优化，根据行数列数大小，时间复杂度为：O(min(m,n)^2*max(m,n))
        # 空间复杂度为：O(max(m,n))
        row, col = len(matrix), len(matrix[0])
        # 如果行数少，扫行
        if row < col:
            return verticalSum(matrix, target)
        # 列数少，扫列
        else:
            return horizontalSum(matrix,target)