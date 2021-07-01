object Solution {

    // 定义一个结构用来记录数组中每个数字出现次数以及出现的始末位置
    case class freqpos(cnt: Int, lp: Int, rp: Int)

    def findShortestSubArray(nums: Array[Int]): Int = {
        var cnt = 0
        var minLen = nums.length
        val hashmap = scala.collection.mutable.Map[Int, freqpos]()

        for (i <- 0 to nums.length - 1) {
            if (hashmap.contains(nums(i))) {
                val temp = hashmap(nums(i))
                hashmap(nums(i)) = freqpos(temp.cnt + 1, temp.lp, i)
            } else {
                hashmap(nums(i)) = freqpos(1, i, i)
            }
        }

        for( (_, info) <- hashmap) {
            if (info.cnt > cnt) {
                cnt = info.cnt
                minLen = info.rp - info.lp + 1
            } else if (info.cnt == cnt) {
                minLen = math.min(minLen, info.rp - info.lp + 1)
            }
        }
        minLen
    }
}