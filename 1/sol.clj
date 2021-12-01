(defn get-lines [file]
  (with-open [rdr (clojure.java.io/reader file)]
    (doall (line-seq rdr))))

(def lines (map #(Integer/parseInt %) (get-lines "./input.txt")))

(defn part1 [lines]
  (loop [l lines p ##Inf res 0]
    (cond
      (empty? l) res
      (< p (first l)) (recur (rest l) (first l) (inc res))
      :else (recur (rest l) (first l) res))))

(defn queue
  ([] (clojure.lang.PersistentQueue/EMPTY))
  ([coll]
    (reduce conj clojure.lang.PersistentQueue/EMPTY coll)))

(defn part2 [coll k]
  (loop [c (drop k coll)
         q (queue (take k  coll))
         s (apply + q) 
         res 0]
    (cond
      (empty? c) res 
      :else (let [ss (+ (- s (peek q)) (first c))]
              (recur (rest c)
                     (conj (pop q) (first c))
                     ss
                     (if (< s ss) (inc res) res))))))

(part1 lines)
(part2 lines 3)
