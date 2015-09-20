# Multiprocessing with Pipe
# Written by Vamei

import multiprocessing as mul
import time

def proc1(pipe):
	print "enter in proc1"
	while True:
		time.sleep(1)
    	pipe.send('hello')
    	print('proc1 rec:',pipe.recv())

def proc2(pipe):
	print "enter in proc2"
	while True:
		print('proc2 rec:',pipe.recv())
    	time.sleep(1)
    	pipe.send('hello, too')

# Build a pipe
pipe = mul.Pipe()

# Pass an end of the pipe to process 1
p1   = mul.Process(target=proc1, args=(pipe[0],))
# Pass the other end of the pipe to process 2
p2   = mul.Process(target=proc2, args=(pipe[1],))
p1.start()
p2.start()

