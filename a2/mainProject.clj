(ns mainProject)

(comment (not x)       -> (nor x))
(comment (and x y)     -> (nor (nor x) (nor y)))
(comment (and x y z)   -> (nor (nor x) (nor y) (nor z)))
(comment (and w x y z) -> (nor (nor w) (nor x) (nor y) (nor z)))
(comment (or x y)      -> (nor (nor x y)))
(comment (or x y z)    -> (nor (nor x y z)))
(comment (or w x y z)  -> (nor (nor w x y z)))
(comment (nor (nor x y false (nor (nor true) (nor (nor (nor (nor z))))))))

(def p1 '(not x))
(def p2 '(and x y))
(def p3 '(and x y z))
(def p4 '(and w x y z))
(def p5 '(or x y))
(def p6 '(or x y z))
(def p7 '(or w x y z))

(def j1 '(nor (nor x)))
(def j2 '(nor (nor (nor x))))
(def j3 '(nor (nor (nor (nor x)))))

(def d1 '(and x (or x (and y (not z)))))
(def d2 '(and (and z false) (or x true false)))
(def d3 '(or true a))
(def d4 '(or x y false (and true (not (not (not z))))))

(def m0 '{})
(def m1 '{x false, z true})
(def m2 '{z true})
(def m3 '{z false})


(defn isTheElementInIt?
  [list element]
  (some #(= element %) list)
  )

(defn deep-substitute [m l]
  (map (fn [i]
         (if (seq? i)
           (deep-substitute m i)
           (m i i)))
       l))

(defn nor_and_help
  [variable]
  (conj (list variable) 'nor)
  )


(defn nor_and
  [a_list]
  (conj (map nor_and_help
             (drop 1 a_list)) 'nor)
  )

(defn nor_or
  [a_list]
  (conj (list (conj (drop 1 a_list) 'nor)) 'nor)
  )

(defn nor_not
  [a_list]
  (conj (drop 1 a_list) 'nor)
  )

(defn nor_conversion_recursive
  [a_list]
  (if (seq? a_list)
    (cond
      (isTheElementInIt? a_list 'or) (nor_or (map (fn [i]
                                                    (if (seq? i)
                                                      (nor_conversion_recursive i)
                                                      i))
                                                  a_list)
                                             )
      (isTheElementInIt? a_list 'and) (nor_and (map (fn [i]
                                                      (if (seq? i)
                                                        (nor_conversion_recursive i)
                                                        i))
                                                    a_list)
                                               )
      :else (nor_not (map (fn [i]
                            (if (seq? i)
                              (nor_conversion_recursive i)
                              i))
                          a_list)
                     )

      )
    a_list
    )

  )


(defn simplify_nor
  [a_list]
  (cond
    (isTheElementInIt? a_list 'true) false
    (some seq? a_list) (if (= 2 (count a_list))
                         (if (= 2 (count (first (drop 1 a_list))))
                           (first (drop 1 (first (drop 1 a_list))))
                           (distinct (remove boolean? a_list))
                           )
                         (distinct (remove boolean? a_list))
                         )
    (= 1 (count (filter symbol? a_list))) true
    :else (distinct (remove boolean? a_list))
    )
  )

(defn recursive_simplify
  [a_list]
  (simplify_nor (map (fn [i]
                       (if (seq? i)
                         (recursive_simplify i)
                         i))
                     a_list))
  )

(defn simplify
  [a_map, a_list]
  (recursive_simplify(nor_conversion_recursive(deep-substitute a_map a_list)))
  )