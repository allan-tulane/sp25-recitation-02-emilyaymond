from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 8
	assert simple_work_calc(20, 3, 2) == 81
	assert simple_work_calc(30, 4, 2) == 256
	assert simple_work_calc(60, 7, 2) == 16807
	assert simple_work_calc(70, 8, 2) == 262144
	assert simple_work_calc(80, 9, 2) == 531441

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(60, 7, 2, lambda n: n) == 27416
	assert work_calc(70, 8, 2, lambda n: n * n) == 524716
	assert work_calc(80, 9, 2, lambda n: n) == 691694

def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	#question 4 test cases
	# work_fn1 = work_calc(2, 2, lambda n: 1)
	# work_fn2 = work_calc(3, 2, lambda n: n)
	# work_fn3 = work_calc(2, 2, lambda n: math.log(n))

	#question 5 test cases
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x**2*math.log(x))

	# work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x ** 2)  # c > log_b(a)
	# work_fn2 = lambda n: work_calc(n,2, 2, lambda x: x ** 0.5) #c < log_b(a)

	# work_fn2 = work_calc(2, 2, lambda n: n ** 2)  # c > log_b(a)
	# work_fn3 = work_calc(2, 2, lambda n: n) #c = log_b(a)
	# work_fn2 = curry_work(2, 2, lambda n: n ** 2) #c > log_b(a)

	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	res = compare_work(work_fn1, work_fn2, sizes)
	print_results(res)
	assert len(res) > 0
	
def test_compare_span():
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: x)
	span_fn2 = lambda n: span_calc(n, 3, 2, lambda x: math.log(x))
	#span_fn2 = curry_span(2, 2, lambda n: math.log(n))
	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	res = compare_span(span_fn1, span_fn2, sizes)
	print_results(res)
	assert len(res) > 0