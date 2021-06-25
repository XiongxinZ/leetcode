object Solution {
    def plusOne(digits: Array[Int]): Array[Int] = {
        var res = Array.concat(Array(0), digits);
        var plus_one = false;

        for (i <- (0 until res.length).reverse if !plus_one) {
            if (res(i) < 9) {
                res(i) += 1;
                plus_one = true;
            } else {
                res(i) = 0;
            }
        }

        if (res(0) == 0) {
            return res.slice(1,res.length);
        }

        return res;
    }
    
}