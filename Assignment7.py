import sys
import random
import math
from math import exp
from math import log

dataFile = sys.argv[1]
f = open(dataFile, 'r');
data = [];
i = 0;
j = 0;
l = f.readline();
while (l != ''):
    a = l.split();
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]));
    data.append(l2);
    l = f.readline();

labelFile = sys.argv[2]
f = open(labelFile, 'r');
trainingLabels = {};
i = 0;
j = 0;
count = {};
count[0] = 0;
count[1] = 0;
l = f.readline();
while (l != ''):
    a = l.split();
    trainingLabels[int(a[1])] = int(a[0])
    if int(a[0]) == 0:
        count[0] += 1;
    else:
        count[1] += 1;
    l = f.readline();
f.close()

for rep in range(0,100):
    test = []
    for a in range(len(data)):
        if (trainingLabels.get(a) != None):
            test.append(data[a])
        
    nrow = len(test)
    nrw = round(nrow*3/5)
    l3 = random.sample(test,nrw)
    rows = len(l3);
    cols = len(l3[0]);
    columns = list(zip(*l3));
    sortedCols={}
    for j in range(0,cols,1):
        sortedCols[j]=sorted(set(columns[j]));
    splitcl = None
    splitvalma = 0
    splitOnColumn = None;
    splitValue = 0
    gini = float('inf')
    ginimain = float('inf')
    for j in range(0,cols,1):
        for i in range(len(sortedCols[j])-1):
            avg=(sortedCols[j][i]+sortedCols[j][i+1])/2;
            lsize = float(0);
            rsize = float(0);
            lp = float(0);
            rp = float(0);
            for k in range (rows):
                if(data[k][j]<avg):
                    if k in trainingLabels:
                        lsize+=1;
                        if (trainingLabels[k]) == 0:
                            lp += 1;
                else:
                    if k in trainingLabels:
                        rsize+=1;
                        if (trainingLabels[k]) == 0:
                            rp += 1;
            if(lsize!=0 and rsize!=0):
                gtemp = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize);
            if gtemp < gini:
                splitOnColumn = j
                splitValue = avg
                gini = gtemp
    if(ginimain>gini):
        ginimain=gini
        splitcl = splitOnColumn
        splitvalma = splitValue
a=0
b=0
for i in range(0,len(data)):
    if i in trainingLabels:
        if(data[i][splitcl]<splitvalma):
            a+=1
        else:
            b+=1
c0=0
c1=1
if(a<b):
    c0=0
    c1=1
else:
    c0=1
    c1=0
    
print(splitvalma," ",splitcl," ", ginimain)
for i in range(0,len(data)):
    if(trainingLabels.get(i)==None):
        sum=0
        for j in range(0,len(data[0])):
            sum+=data[i][j]
        avgs = (sum/len(data[0]))
        if(data[i][splitcl]<splitvalma):
            print(c0,i)
        else:
            print(c1,i)