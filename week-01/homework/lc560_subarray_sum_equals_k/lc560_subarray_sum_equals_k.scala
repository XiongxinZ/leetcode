object Solution {
    def subarraySum(nums: Array[Int], k: Int): Int = {
        var nums_sum = 0
        var count = 0
        var nums_sum_array = Array[Int]()
        nums.map(x => {
            nums_sum = nums_sum + x
            nums_sum_array = nums_sum_array :+ nums_sum
        })

        // 先求出直接等于k的nums_sum个数
        count = nums_sum_array.filter(x => x == k).length


        for(j <- Range(0, nums_sum_array.length)) {
            // upper bound
            for (i <- (j + 1) until nums_sum_array.length) {
                // 再找出所有满足s[i] - s[j] = k的个数 (j > 0)
                if (nums_sum_array(i) - nums_sum_array(j) == k) {
                    count = count + 1
                }
            }
        }
        count
    }
}