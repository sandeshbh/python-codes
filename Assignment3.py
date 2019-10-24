import sys
import random
import math

def dot_product(w, data):
    dp = 0
    dp = sum(x*y for x,y in zip(w,data))
    return dp

datafile = sys.argv[1]

f = open(datafile, 'r')
data = []
l = f.readline()

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])


print("Rows= ", rows, " cols = ", cols)

f.close()

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    if (trainlabels[a[1]] == 0):
        trainlabels[a[1]] = -1;
    l = f.readline()

    n[int(a[0])] += 1

f.close()

w = []
for j in range(0, cols, 1):
    w.append(0.02 * random.random() - 0.01)


eta = 0.001
hingLoss = rows * 10
diff = 1
count = 0

while ((diff) > 0.001):
    dellf = [0] * cols
    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            condition = (trainlabels.get(str(j)) * (dot_product(w, data[j])))
            for k in range(0, cols, 1):
                if (condition < 1):
                    dellf[k] += -1 * ((trainlabels.get(str(j))) * data[j][k])
                else:
                    dellf[k] += 0


    for j in range(0, cols, 1):
        w[j] = w[j] - eta * dellf[j]
    prev = hingLoss
    hingLoss = 0


    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            hingLoss += max(0, 1 - (trainlabels.get(str(j)) * dot_product(w, data[j])))

        diff = abs(prev - hingLoss)


normW = 0
for i in range(0, (cols - 1), 1):
    normW += w[i] ** 2

normW = math.sqrt(normW)


d_orgin = abs(w[len(w) - 1] / normW)

print ("Distance to origin = " + str(d_orgin))


for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) == None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("1 ", i)
        else:
            print("0 ", i)
