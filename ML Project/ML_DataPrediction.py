
####### Ashish Chhabbi(ahc32) #########
####### Sandesh Bhaiswar(ssb84) #######

import random
import sys
import time
import os
from sklearn.svm import LinearSVC

def calculateFeatures(data, labels):

    linearSVC = LinearSVC(C=0.0024, penalty='l1', dual=False).fit(data, [x[0] for x in labels])
    score = linearSVC.coef_

    feature = []
    feature_Cols = []
    for k in range(len(score[0])):
        if (score[0][k] != 0.0):
            feature_Cols.append(int(k))
            rowdata = []
            for i in range(len(data)):
                rowdata.append(data[i][k])
            feature.append(rowdata)
    bestFeatures_Data = [list(map(float, x)) for x in zip(*feature)]
    print ("\nBest Feature Columns:\n",feature_Cols)
    return bestFeatures_Data, feature_Cols

def getFeatures(testdata, feature_Cols):

    bstFeature = []
    totalFeatures = len(feature_Cols)

    for rows in range(len(testdata)):
        col = []
        k = 0
        for columns in range(len(testdata[0])):
            if (k < totalFeatures and feature_Cols[k] == columns):
                col.append(testdata[rows][columns])
                k = k + 1
        bstFeature.append(col)
    return bstFeature

def predictLabels(trainData, trainLabels, testData):
    clf = LinearSVC(max_iter=15000000, tol=0.00000001).fit(trainData, [x[0] for x in trainLabels])
    predictedLabels = clf.predict((testData))

    predictedLabels_File = open(os.getcwd () + '/predictedLabels', 'w')

    for i in range(0, len(testData), 1):
        predictedLabels_File.write(str(predictedLabels[i]) + " " + str(i) + '\n')

    predictedLabels_File.close()
    print("Predicted Labels File Generated!")
    return True

def mainProgram():
    trainData = []
    file1 = sys.argv[1]
    with open(file1) as trainingdata:
        for line in trainingdata:
            trainData.append([int(l) for l in line.split()])

    trainLabels = []
    file2 = sys.argv[2]
    with open(file2) as trainingLabels:
        for line in trainingLabels:
            trainLabels.append([int(l) for l in line.split()])

    testdata = []
    file3 = sys.argv[3]
    with open(file3) as testingData:
        for line in testingData:
            testdata.append([int(l) for l in line.split()])

    bestfeatures_data, feature_cols = calculateFeatures(trainData, trainLabels)
    bestfeature_testdata = getFeatures(testdata, feature_cols)
    isPredicted = predictLabels(bestfeatures_data, trainLabels, bestfeature_testdata)
mainProgram()
