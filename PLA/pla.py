import numpy as np

def pla():

	data = np.loadtxt('data.txt', dtype=np.float32)
	data_y = np.copy(data[:,-1])
	data_x = np.roll(data, 1, axis=1)
	data_x[:,0] = np.ones(len(data_x)) # set x0 = 1

	W = np.zeros(data_x.shape[1]) # initial W

	iteration = 0
	while True:
		err = 0
		for x, y in zip(data_x, data_y):
			if np.dot(W, x)*y<=0:
				err+=1
				iteration+=1
				W+=x*y

		if err==0:
			break

	print("%d times: " % (iteration), W)


if '__main__'==__name__:
	pla()
