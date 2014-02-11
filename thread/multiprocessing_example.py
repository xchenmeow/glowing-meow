import multiprocessing

def f(name):
	print 'hello', name

def worker(num):
	print 'Worker: ', num
	return

if __name__ == '__main__':
	# p = Process(target=f, args=('bob',))
	# p.start()
	# p.join()

	jobs = []
	for i in xrange(1, 5):
		p = multiprocessing.Process(target=worker, args=(i, ))
		jobs.append(p)
		p.start()