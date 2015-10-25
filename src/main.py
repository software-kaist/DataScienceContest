'''
Created on 2015. 10. 24.

@author: SUNgHOOn
'''

from numpy import ones
from numpy import log
#import array

# 정규식으로 단어별 파싱 함수
def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 0] 

# 중복을 제거한 단어 모음 함수
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set 중복 허용 안함!!
    for document in dataSet:
        print(document)
        vocabSet = vocabSet | set(document) #union of the two sets
        
    vocabSet.remove("hwt")
    vocabSet.remove("swt")
    vocabSet.remove("etc")
    return list(vocabSet)

def whiteVocabList():
    vocabSet = set([])  #create empty set 중복 허용 안함!!
    vocabSet.add("replace")
    vocabSet.add("replaced")
    vocabSet.add("replacement")
    vocabSet.add("steering")
    vocabSet.add("gears")
    vocabSet.add("telescopic")
    vocabSet.add("escort")
    vocabSet.add("abs")
    vocabSet.add("cabs")
    vocabSet.add("escalade")
    vocabSet.add("automatic")
    vocabSet.add("automatically")
    vocabSet.add("inspect")
    vocabSet.add("inspection")
    vocabSet.add("inspections")
    vocabSet.add("inspecting")
    vocabSet.add("inspected")
    vocabSet.add("units")
    vocabSet.add("unit")
    vocabSet.add("bolts")
    vocabSet.add("coolant")
    vocabSet.add("lines")
    vocabSet.add("line")
    vocabSet.add("door")
    vocabSet.add("software")
    vocabSet.add("crack")
    vocabSet.add("cracks")
    vocabSet.add("cracking")
    vocabSet.add("cracked")
    vocabSet.add("insulation")
    vocabSet.add("gunite")
    vocabSet.add("insulation")
    vocabSet.add("calibration")
    vocabSet.add("absorber")
    vocabSet.add("absorbers")
    vocabSet.add("absorb")
    vocabSet.add("ecu")
    vocabSet.add("tpms")
    vocabSet.add("absolute")
    vocabSet.add("telescopic")
    vocabSet.add("monitoring")
    vocabSet.add("hecu")
    vocabSet.add("absence")
    vocabSet.add("remove")
    vocabSet.add("overheated")
    vocabSet.add("exhoust")
    vocabSet.add("components")
    vocabSet.add("component")
    vocabSet.add("melt")
    vocabSet.add("illuminates")
    vocabSet.add("illuminate")
    vocabSet.add("update")
    vocabSet.add("updated")
    vocabSet.add("absorption")
    vocabSet.add("Tire pressure monitoring systems")
    vocabSet.add("esc")
    vocabSet.add("escape")
    vocabSet.add("escapes")
    vocabSet.add("upload")
    vocabSet.add("rescue")
    vocabSet.add("describing")

    return list(vocabSet)

# 단어별 빈도수 구하기
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

# 나이브 베이지안 
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
#     print(numTrainDocs, numWords)
#     print(sum(trainCategory))
#     pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
#     print(p0Num, len(p0Num))
#     print(p1Num, len(p1Num))
    p0Denom = 2.0; p1Denom = 2.0  
    abus = 0                      #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == "hwt":
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
            abus += 1
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        
    pAbusive = abus/float(numTrainDocs)
#         print(p0Num, len(p0Num))
#         print(p0Denom)
#         print(p1Num, len(p1Num))
#         print(p1Denom)
        
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    
    #print(p1, p0)
    if p1 > p0:
        return "hwt"
    else: 
        return "swt"


if __name__ == '__main__':
    '''
    학습 
    '''
    docList=[]; classList = [];
    recall_2014_file = open("../new_rcl_out_14.txt", "r", encoding='utf8')
    #recall_2014_file = open("../test_set.txt", "r", encoding='utf8')
    for line in recall_2014_file:
        line = line.strip()
        wordList = textParse(line)
        docList.append(wordList)
        
    # 중복 제거하여 단어 리스트 만듬
    #vocabList = createVocabList(docList)
    vocabList = whiteVocabList()
    print(vocabList)
    
    trainMat=[]; trainClasses = []
    for docIndex in range(len(docList)):
        # 등장 빈도 수 체크 vocabList trainMat 같은 인덱스로 묶임!!
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(docList[docIndex][0])
#         print(trainMat[docIndex])
#         print(trainClasses)
        
    # 학습된 테이블
    p0V,p1V,pSpam = trainNB0((trainMat), (trainClasses))
    
    # 학습된 테이블 검증
    testDocList=[]; classList = [];
    
    ''' 
    테스트 할 파일  로딩
    '''
    recall_2014_file_test = open("../new_rcl_out_14.txt", "r", encoding='utf8')
    #recall_2014_file_test = open("../test_set.txt", "r", encoding='utf8')
    for line in recall_2014_file_test:
        line = line.strip()
        wordList = textParse(line)
        testDocList.append(wordList)
    
    error_cnt = 0
    for i in range(len(testDocList)):
        wordVector = bagOfWords2VecMN(vocabList, testDocList[i])
        predic = classifyNB(wordVector,p0V,p1V,pSpam)
        if predic != testDocList[i][0]:
            error_cnt += 1
            print ("classification error", testDocList[i][0], predic)
        else:
            print ("classification OK", testDocList[i][0], predic)
             
    print(error_cnt, error_cnt/len(testDocList))
    # print(len(docList))
    # print(vocabList)