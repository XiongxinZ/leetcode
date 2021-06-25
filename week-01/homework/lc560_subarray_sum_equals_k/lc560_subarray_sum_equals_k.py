class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_sum_dict = {}
        nums_sum = count = 0
        # i <- 1..n, j <- 1..i，几个s[i] - s[j] = k
        for num in nums:
            nums_sum += num

            # 当s[j] = 0, s[i] = k有且仅有一个
            if nums_sum == k:
                count += 1
            # 当s[j] > 0, 有几个s[j]满足s[j] = s[i] - k
            if nums_sum - k in nums_sum_dict:
                count += nums_sum_dict[nums_sum-k]

            # 后置存储nums_sum的个数，避免k=0的情况
            if nums_sum in nums_sum_dict:
                nums_sum_dict[nums_sum] += 1
            else:
                nums_sum_dict[nums_sum] = 1
        return count