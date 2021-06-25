class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 添加一个可能最高位，以防后面进位
        ans = [0] + digits

        # 从末尾开始+1，向前加直到不能进位为止
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] < 9:
                ans[i] += 1
                break

            ans[i] = 0
        
        if ans[0] == 0:
            return ans[1:]
        else:
            return ans