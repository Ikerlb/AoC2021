(require '[clojure.string :as string])

(defn get-lines [file]
  (with-open [rdr (clojure.java.io/reader file)]
    (doall (line-seq rdr))))

(defn parse-line [line]
  (let [[d i] (string/split line #" ")]
    [d (Integer/parseInt i)]))

(def lines
  (map parse-line (get-lines "./input.txt")))

(defn step-part1 [x y cmd i]
  (cond
    (= cmd "forward") [(+ x i) y]
    (= cmd "up") [x (- y i)]
    :else [x (+ y i)]))

(defn step-part2 [x y aim cmd i]
  (cond
    (= cmd "forward") [(+ x i) (- y (* aim i)) aim]
    (= cmd "up") [x y (+ aim i)]
    :else [x y (- aim i)]))

;; list of commands, init vector, step function to reduce
(defn solve [cmds init step-fn]
  (reduce #(apply step-fn (into %1 %2)) init cmds))

(apply * (solve lines [0 0] step-part1))
(apply * (take 2 (solve lines [0 0 0] step-part2)))
