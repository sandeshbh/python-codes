import sys

datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
i = 0
l = f.readline()

while (l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()


labelfile = sys.argv[2]
f = open(labelfile, 'r')
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()
while (l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()

m0 = []
m1 = []
for i in range(0, cols, 1):
	m0.append(1)
	m1.append(1)

for i in range(0, rows, 1):
	if(trainlabels.get(i) != None and trainlabels[i] == 0):
		n[0] += 1
		for j in range(0, cols, 1):
			m0[j] += data[i][j]

	if(trainlabels.get(i) != None and trainlabels[i] == 1):
		n[1] += 1
		for j in range(0, cols, 1):
			m1[j] += data[i][j]

for j in range(0, cols, 1):
	m0[j] = m0[j]/n[0]
	m1[j] = m1[j]/n[1]

std0 = []
std1 = []
for i in range(0, cols, 1):
	std0.append(0)
	std1.append(0)

for i in range(0, rows, 1):
	if(trainlabels.get(i) != None and trainlabels[i] == 0):
		for j in range(0, cols, 1):
			std0[j] += (m0[j] - data[i][j])**2
	if(trainlabels.get(i) != None and trainlabels[i] == 1):
		for j in range(0, cols, 1):
			std1[j] += (m1[j] - data[i][j])**2

for j in range(0, cols, 1):
	std0[j] /= n[0]
	std1[j] /= n[1]

for i in range(0, rows, 1):
	if(trainlabels.get(i) == None):
		d0 = 0
		d1 = 0
		for j in range(0, cols, 1):
			d0 += ((data[i][j] - m0[j])**2)/std0[j]
			d1 += ((data[i][j] - m1[j])**2)/std1[j]
		if (d0 < d1):
			print('0 ', i)
		else:
			print('1 ', i)