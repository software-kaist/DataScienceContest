import sys
def process_file(fileName):
    input_file = open(fileName, "r")
    for line in input_file:
        line = line.strip()
        print (line)
        
    input_file.close()
    
import random
def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

import math
def mean(numbers):
    return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.iteritems():
        summaries[classValue] = summarize(instances)
    return summaries

import math
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

dataset = [[1], [2], [3], [4], [5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
print('Split {0} rows into train with {1} and test with {2}').format(len(dataset), train, test)

dataset = [[1,20,1], [2,21,0], [3,22,1]]
separated = separateByClass(dataset)
print('Separated instances: {0}').format(separated)

numbers = [1,2,3,4,5]
print('Summary of {0}: mean={1}, stdev={2}').format(numbers, mean(numbers), stdev(numbers))

dataset = [[1,20,0], [2,21,1], [3,22,0]]
summary = summarize(dataset)
print('Attribute summaries: {0}').format(summary)

dataset = [[1,20,1], [2,21,0], [3,22,1], [4,22,0]]
summary = summarizeByClass(dataset)
print('Summary by class value: {0}').format(summary)

x = 71.5
mean = 73
stdev = 6.2
probability = calculateProbability(x, mean, stdev)
print('Probability of belonging to this class: {0}').format(probability)


process_file("../FLAT_RCL_Out_14.txt")

# import random    
# 
# # 게임을 위한 랜덤 숫자 생성
# rn = ["0", "0", "0"]
# rn[0] = str(random.randrange(1, 9, 1))
# rn[1] = rn[0]
# rn[2] = rn[0]
# while (rn[0] == rn[1]):
#     rn[1] = str(random.randrange(1, 9, 1))
# while (rn[0] == rn[2] or rn[1] == rn[2]):
#     rn[2] = str(random.randrange(1, 9, 1))
# 
# #print(rn)
# 
# t_cnt = 0 # 시도횟수
# s_cnt = 0 # 스트라이크 갯수
# b_cnt = 0 # 볼 갯수
# 
# print("숫자야구게임을 시작합니다 !!!")
# print("---------------------------")
# while ( s_cnt < 3 ):
# 
#     num = str(input("숫자 3자리를 입력하세요 : "))
# 
#     s_cnt = 0
#     b_cnt = 0
# 
#     for i in range(0, 3):
#         for j in range(0, 3):
#             if(num[i] == str(rn[j]) and i == j):
#                 s_cnt += 1
#             elif(num[i] == str(rn[j]) and i != j):
#                 b_cnt += 1
#     print("결과 : [", s_cnt, "] Strike [", b_cnt, "] Ball")
#     t_cnt += 1
# print("---------------------------")
# print(t_cnt, "번 만에 정답을 맞추셨습니다.")