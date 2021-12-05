(require '[clojure.string :as string])

(defn get-lines [file]
  (with-open [rdr (clojure.java.io/reader file)]
    (doall (line-seq rdr))))

(defn parse-point [s]
  (map #(Integer/parseInt %) (string/split s #",")))

(defn parse-segment [line]
  (flatten
    (map
      parse-point
      (string/split line #" -> "))))

(defn span [sx sy ex ey]
  (let [dx (delta sx ex)
        dy (delta sy ey)]
    (take-while #(not (= (list (+ ex dx) (+ ey dy)) %))
                (iterate
                  #(list (+ (nth % 0) dx) (+ (nth % 1) dy))
                  (list sx sy)))))

(defn into-counter [c point]
  (let [[sx sy ex ey] point]
    (reduce
      #(if
         (contains? %1 %2)
         (update %1 %2 inc)
         (assoc %1 %2 1))
      c
      (span sx sy ex ey))))

(defn points-counter [segments]
  (reduce
    #(into-counter %1 %2)
    {}
    segments))

(defn delta [n1 n2]
  (cond
    (pos? (- n2 n1)) 1 
    (zero? (- n2 n1)) 0
    :else -1))


(defn horizontal-and-vertical [segments]
  (filter
    #(let
       [[sx sy ex ey] %]
       (or (== sx ex) (== sy ey)))
    segments))


(defn more-than-one-time [counter]
  (filter #(let [[_, v] %]
             (>= v 2))
          counter))

(let [segments (map parse-segment (get-lines "input.txt"))]
  (do (println
        (count
          (more-than-one-time (points-counter (horizontal-and-vertical segments)))))
      (println
        (count
          (more-than-one-time (points-counter segments))))))
