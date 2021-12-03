(defn get-lines [file]
  (with-open [rdr (clojure.java.io/reader file)]
    (doall (line-seq rdr))))

(defn get-bit 
  [n k]
  (if (== (bit-and n (bit-shift-left 1 k)) 0) 0 1))

(defn count-kth-bits
  [nums k]
  (reduce #(update %1 (get-bit %2 k) inc) {0 0 1 0} nums))

(defn max-key-by-value
  [m]
  (apply max-key m (keys m)))

(defn min-key-by-value
  [m]
  (apply min-key m (keys m)))

(defn to-decimal [coll]
  (apply + (map-indexed #(if (== %2 0) 0 (bit-shift-left 1 %1)) coll)))

(defn selector
  [cnt f rating]
  (cond
    (and (== (cnt 0) (cnt 1)) (= rating "oxygen")) 1
    (== (cnt 0) (cnt 1)) 0
    :else (f cnt)))

(defn filter-until-one
  [nums n f r]
  (loop [nums nums k (dec n)]
    (cond
      (<= (count nums) 1) nums
      :else (let [cnt (count-kth-bits nums k)
                  sel (selector cnt f r)]
              (recur
                (filter #(== (get-bit % k) sel) nums)
                (dec k))))))


(let [lines (get-lines "./input.txt")
      nums (map #(Integer/parseInt % 2) lines)
      n (count (first lines))
      count-bits (map #(count-kth-bits nums %) (range n))
      gamma (to-decimal (map max-key-by-value count-bits))
      epsilon (to-decimal (map min-key-by-value count-bits))
      oxygen (filter-until-one nums n max-key-by-value "oxygen")
      co2 (filter-until-one nums n min-key-by-value "co2")]
  (do
    (println (* gamma epsilon))
    (println (* (nth oxygen 0) (nth co2 0)))))
