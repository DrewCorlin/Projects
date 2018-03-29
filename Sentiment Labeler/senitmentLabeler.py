import glob
import re
import math
import numpy

def main():
    X_train, Y_train, X_test, Y_test = readData(0.67)
    trained_model = train(X_train, Y_train, {'smoothparam' : 0.1})
    Y_pred = test(X_test, trained_model)
    eval = str(evaluate(Y_test, Y_pred))
    print 'The error rate of my classifier is ' + eval

def readData(ratio):
    xTrain, xTest, yTrain, yTest = {}, {}, [], []
    trainingLengthSeen = 0
    testLengthSeen = 0
    for filename in glob.iglob('./data/*.txt'):
        file = open(filename, 'r')
        numLines = sum(1 for line in file)
        file.close()
        threshold = int(math.floor(numLines * ratio))
        xTrain, yTrain = vectorize(xTrain, yTrain, 0, threshold + 1, filename, trainingLengthSeen)
        xTest, yTest = vectorize(xTest, yTest, threshold, numLines + 1, filename, testLengthSeen)
        trainingLengthSeen += threshold
        testLengthSeen += numLines - threshold
    return xTrain, yTrain, xTest, yTest

def cleanString(s):
    return re.sub('[^a-zA-Z ]+', '', s).lower()

def getLabel(s):
    return int(s.replace('\n','').replace('\r','')[-1]) #last element in list

def vectorize(feature, label, minLine, maxLines, filename, lengthSeen):
    count = 0
    file = open(filename,'r')
    for line in file:
        count += 1
        if count <= minLine:
            continue
        if count >= maxLines:
            break
        label.append(getLabel(line))
        words = list(set(cleanString(line).rstrip().split(' '))) #create an iterable set
        for word in words:
            if word in feature:
                feature.get(word).append(1)
            else:
                temp = []
                for x in range(minLine, lengthSeen + count - 1):
                    temp.append(0)
                temp.append(1)
                feature[word] = temp
        for key, value in feature.iteritems():
            if len(value) < (count - minLine) + lengthSeen:
                value.append(0)
    file.close()
    return feature, label

def train(X_train, Y_train, train_opt):
    smoothFactor = train_opt['smoothparam']
    vocabSize = len(X_train.keys())
    model = dict.fromkeys(X_train, [])
    
    posProbLabel = sum(Y_train) / float(len(Y_train))
    negProbLabel = 1 - posProbLabel
    
    for word, val in X_train.items():
        posProbX, negProbX = 0.0, 0.0
        for wordAppears, numY in zip(val, Y_train):
            if wordAppears == 1:
                if numY == 1:
                    posProbX += 1
                if numY == 0:
                    negProbX +=1

    posProbSentiment = (posProbX/len(Y_train) + smoothFactor) / (posProbLabel + (smoothFactor * vocabSize))
        negProbSentiment = (negProbX/len(Y_train) + smoothFactor) / (negProbLabel + (smoothFactor * vocabSize))
        
        model[word] = {"pos": 0, "neg": None} if posProbSentiment == 0 else {"pos": math.log(posProbSentiment, 10), "neg": None}
        model[word]["neg"] = 0 if negProbSentiment == 0 else  math.log(negProbSentiment, 10)

return model

def test(X_test, model):
    predPosY = [0.0] * len(X_test.items()[0][1])
    predNegY = [0.0] * len(X_test.items()[0][1])
    intersection = [i for i in X_test if i in model]
    for wordX, value in X_test.items():
        if wordX in intersection:
            for index, val in enumerate(value):
                if val == 1:
                    predPosY[index] += model[wordX]["pos"]
                    predNegY[index] += model[wordX]["neg"]
    return numpy.greater(predPosY, predNegY).astype(int)


def evaluate(Y_test, Y_pred):
    return 1 - sum(numpy.equal(Y_test, Y_pred).astype(int)) / float(len(Y_test))

main()







