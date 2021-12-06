(require '[clojure.string :as string])

(defn get-lines [file]
  (with-open [rdr (clojure.java.io/reader file)]
    (doall (line-seq rdr))))

(defn to-int-list
  [line]
  (map #(Integer/parseInt %) (string/split line #",")))

(defn add-to-counter
  [c n]
  (cond
    (contains? c n) (update c n inc)
    :else (assoc c n 1)))

(defn counter
  [coll]
  (reduce #(add-to-counter %1 %2) {} coll))

(defn step
  [q]
  (let [n (.getFirst q)
        lst (.removeLast q)
        snd-to-last (.removeLast q)]
    (do
      (.addLast q (+ n snd-to-last))
      (.addLast q (+ lst))
      (.addLast q (.removeFirst q))
      q)))

(defn get-or-default
  [m n d]
  (cond
    (contains? m n) (m n)
    :else d))

;; i don't quite like java interop
;; but i guess its better to have 
;; than not having it at all
(defn init-deque
  [c]
  (reduce
    #(do (.addLast %1 (get-or-default c %2 0)) %1)
    (new java.util.LinkedList)
    (range 9)))

(defn steps
  [c n]
  (nth
    (iterate step (init-deque c))
    n))

(let [l (to-int-list (first (get-lines "input.txt")))
      c (counter l)] 
  (do
    (println (apply + (steps c 80)))
    (println (apply + (steps c 256)))))
