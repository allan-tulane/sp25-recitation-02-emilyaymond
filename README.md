# CMPS 2200  Recitation 02

**Name (Team Member 1):**______Emily Aymond___________________  
**Name (Team Member 2):**_______Camden Yale__________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

|     n |   W(n) (f=1) |   W(n) (f=log n) |   W(n) (f=n) |
|-------|--------------|------------------|--------------|
|    10 |           15 |            8.294 |           36 |
|    20 |           31 |           19.584 |           92 |
|    50 |           63 |           52.201 |          276 |
|   100 |          127 |          109.008 |          652 |
|  1000 |         1023 |          959.608 |         9120 |
|  5000 |         8191 |         5823.326 |        61728 |
| 10000 |        16383 |        11655.862 |       133456 |


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**Case 1**

$c < \log_b a$

work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)

work_fn2 = lambda n: work_calc(n,2, 2, lambda x: x ** 0.5)

 |     n |    W_1 |       W_2 |
|-------|--------|-----------|
|    10 |     36 |    21.291 |
|    20 |     92 |    47.055 |
|    50 |    276 |   110.236 |
|   100 |    652 |   230.472 |
|  1000 |   9120 |  2075.117 |
|  5000 |  61728 | 14251.208 |
| 10000 | 133456 | 28602.416 |


**Case 2**

$c > \log_b a$

work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)

work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x ** 2)

|     n |    W_1 |       W_2 |
|-------|--------|-----------|
|    10 |     36 |       174 |
|    20 |     92 |       748 |
|    50 |    276 |      4790 |
|   100 |    652 |     19580 |
|  1000 |   9120 |   1990744 |
|  5000 |  61728 |  49957880 |
| 10000 | 133456 | 199915760 |

**Case 3**

$c = \log_b a$

work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)

work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x**2*math.log(x))

|     n |    W_1 |            W_2 |
|-------|--------|----------------|
|    10 |     36 |        329.821 |
|    20 |     92 |       1857.934 |
|    50 |    276 |      15941.185 |
|   100 |    652 |      77934.073 |
|  1000 |   9120 |   12412644.897 |
|  5000 |  61728 |  391099205.643 |
| 10000 | 133456 | 1703232448.484 |




- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**Case 1**

span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
span_fn2 = lambda n: span_calc(n, 3, 2, lambda x: x)

|     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |     4 |    18 |
|    20 |     5 |    38 |
|    50 |     6 |    97 |
|   100 |     7 |   197 |
|  1000 |    10 |  1994 |
|  5000 |    13 |  9995 |
| 10000 |    14 | 19995 |

**Case 2**

span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
span_fn2 = lambda n: span_calc(n, 3, 2, lambda x: math.log(x))

|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |     4 |  5.605 |
|    20 |     5 |  8.601 |
|    50 |     6 | 13.506 |
|   100 |     7 | 18.111 |
|  1000 |    10 | 37.786 |
|  5000 |    13 | 56.944 |
| 10000 |    14 | 66.154 |

The complexity of this case will be 


