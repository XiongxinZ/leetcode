object Solution {
    def subdomainVisits(cpdomains: Array[String]): List[String] = {
        import scala.collection.mutable
        var map = mutable.Map[String, Int]()
        for (visit <- cpdomains) {
            var count = visit.split(" ")(0).toInt
            var domains: Array[String] = visit.split(" ")(1).split("\\.")
            var cname = ""
            for(i <- (0 until domains.size).reverse) {
                cname = domains(i) + "." + cname
                // 去除字符中最后一个"."比如mail.google.com.中com后面的"."
                var key = cname.substring(0, cname.length() - 1)
                if (map.contains(key)) {
                    map += (key -> (map.get(key).get + count) )
                } else {
                    map += (key -> count)
                }
            }
        }

        var ret = new scala.collection.mutable.ListBuffer[String]()
        map.foreach(x => ret += x._2 + " " + x._1)
        ret.toList
    }
}