(require '[clojure.string :as string])

(defn get-lines [file]
  (with-open [rdr (clojure.java.io/reader file)]
    (doall (line-seq rdr))))

(defn parse-line [line]
  (let [[d i] (string/split line #" ")]
    [d (Integer/parseInt i)]))

(def lines
  (map parse-line (get-lines "./input.txt")))

(defn step1 [x y cmd i]
  (cond
    (= cmd "forward") [(+ x i) y]
    (= cmd "up") [x (- y i)]
    :else [x (+ y i)]))

(defn step2 [x y aim cmd i]
  (cond
    (= cmd "forward") [(+ x i) (- y (* aim i)) aim]
    (= cmd "up") [x y (+ aim i)]
    :else [x y (- aim i)]))
    
(defn part1 [cmds sx sy]
  (reduce #(let [[x y] %1
                 [cmd i] %2]
             (step1 x y cmd i)) [sx sy] cmds))

(defn part2 [cmds sx sy sa]
  (reduce #(let [[x y a] %1
                 [cmd i] %2]
             (step2 x y a cmd i)) [sx sy sa] cmds))

(apply * (part1 lines 0 0))
(apply * (take 2 (part2 lines 0 0 0)))
