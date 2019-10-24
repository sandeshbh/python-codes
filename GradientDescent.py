import sys
import random
import math


def DotProduct(w, data):
	dp = 0
	dp = sum(x*y for x,y in zip(w,data))
	return dp


dataFile1 = sys.argv[1]
#print(dataFile1)
f1 = open(dataFile1, 'r')
data = []
i = 0
l1 = f1.readline()
while (l1 != ''):
	a1 = l1.split()
	l2 = []
	for j in range(0, len(a1), 1):
		l2.append(float(a1[j]))

	l2.append(1.0)
	data.append(l2)
	l1 = f1.readline()


dataFile2 = sys.argv[2]
#print(dataFile2)
f2 = open(dataFile2, 'r')

train = {}
l3 = f2.readline()
while (l3 != ''):
	a2 = l3.split()
	train[int(a2[1])] = int(a2[0])
	l3 = f2.readline()



rows = len(data)
cols = len(data[0])
for i in train:
	if train[i] == 0:
		train[i]=-1


w = []

for i in range(0, cols):
	w.append(0.02 * random.random() - 0.01)

#print(w)


j1 = 0
for i in range(0, rows):
	if(train.get(i) != None):
		j1 += (train[i] - DotProduct(w, data[i]))**2
		#print(j1)

#print('j ' + str(j1))

eta = 0.001


#Gradient Descent

converged = False
dp = 0
dp1 = 0
while not converged:
	dellF = [0]*cols
	for i in range(0,rows):
		if(train.get(i) != None):
			dp = DotProduct(w, data[i])
			for j in range(0, cols):
				dellF[j] += (train[i] - dp)*data[i][j]

	for k in range(0, cols):
		w[k] += eta * dellF[k]

	error = 0

	for t in range(0, rows):
		if (train.get(t) != None):
			dp1 = DotProduct(w, data[t])
			error += (train[t] - dp1)**2
			#print(dp1)

	#error=error/2
	#print("Error is %.4f" % error)
	if abs(j1-error) <= 0.001:
		converged = True
		print("Converged")

	#print('Iterations: ' + str(iteration))
	#print(iteration1)

	j1 = error


print('w0 is ' + str(w[0]))
print('w1 is ' + str(w[1]))


normW = 0
for i in range(0, cols-1):
	normW += w[i]**2

print("Normal Weight " + str(normW))
normW = math.sqrt(normW)

d_origin = abs(w[len(w)-1]/normW)
print('The origin is: ' + str(d_origin))


#Prediction
for i in range(0, rows):
	if (train.get(i) == None):
		#print('Test point' + str(data[i]))
		#print('w is '+ str(w))
		dp = DotProduct(w, data[i])
		if(dp > 0):
			print('1 ', i)

		else:
			print('0 ', i)