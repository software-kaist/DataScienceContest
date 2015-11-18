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
    vocabSet.add('leak')
    vocabSet.add('inspect')
    vocabSet.add('damaged')
    vocabSet.add('detaches')
    vocabSet.add('locked')
    vocabSet.add('corrected')
    vocabSet.add('installed')
    vocabSet.add('melting')
    vocabSet.add('install')
    vocabSet.add('causing')
    vocabSet.add('impact')
    vocabSet.add('incorrect')
    vocabSet.add('event')
    vocabSet.add('repair')
    vocabSet.add('overloaded')
    vocabSet.add('affected')
    vocabSet.add('remove')
    vocabSet.add('protected')
    vocabSet.add('disengaged')
    vocabSet.add('misaligned')
    vocabSet.add('fmvss')
    vocabSet.add('eps')
    vocabSet.add('system')
    vocabSet.add('control')
    vocabSet.add('unit')
    vocabSet.add('module')
    vocabSet.add('updated')
    vocabSet.add('electronic')
    vocabSet.add('version')
    vocabSet.add('recalibrate')
    vocabSet.add('reflash')
    vocabSet.add('receives')
    vocabSet.add('algorithm')
    vocabSet.add('interface')
    vocabSet.add('diagnostics')
    vocabSet.add('calibrations')
    vocabSet.add('recalibrated')
    vocabSet.add('reprogrammed')
    vocabSet.add('controlling')
    vocabSet.add('dbna')
    vocabSet.add('esc')
    vocabSet.add('eco')
    vocabSet.add('ewps')
    vocabSet.add('bcm')
    vocabSet.add('ecx')
    vocabSet.add('pcm')
    vocabSet.add('vim')
    vocabSet.add('ecu')
    vocabSet.add('programming')
    vocabSet.add('monitoring')
    vocabSet.add('disabled')
    vocabSet.add('reprogram')
    vocabSet.add('westport')
    vocabSet.add('tpms')
    vocabSet.add('upload')
    vocabSet.add('calibration')
    vocabSet.add('ecm')
    vocabSet.add('software')
    vocabSet.add('update')




#     vocabSet.add("replace")
#     vocabSet.add("replaced")
#     vocabSet.add("replacement")
#     vocabSet.add("steering")
#     vocabSet.add("gears")
#     vocabSet.add("telescopic")
#     vocabSet.add("escort")
#     vocabSet.add("abs")
#     vocabSet.add("cabs")
#     vocabSet.add("escalade")
#     vocabSet.add("automatic")
#     vocabSet.add("automatically")
#     vocabSet.add("inspect")
#     vocabSet.add("inspection")
#     vocabSet.add("inspections")
#     vocabSet.add("inspecting")
#     vocabSet.add("inspected")
#     vocabSet.add("units")
#     vocabSet.add("unit")
#     vocabSet.add("bolts")
#     vocabSet.add("coolant")
#     vocabSet.add("lines")
#     vocabSet.add("line")
#     vocabSet.add("door")
#     vocabSet.add("software")
#     vocabSet.add("crack")
#     vocabSet.add("cracks")
#     vocabSet.add("cracking")
#     vocabSet.add("cracked")
#     vocabSet.add("insulation")
#     vocabSet.add("gunite")
#     vocabSet.add("insulation")
#     vocabSet.add("calibration")
#     vocabSet.add("absorber")
#     vocabSet.add("absorbers")
#     vocabSet.add("absorb")
#     vocabSet.add("ecu")
#     vocabSet.add("tpms")
#     vocabSet.add("absolute")
#     vocabSet.add("telescopic")
#     vocabSet.add("monitoring")
#     vocabSet.add("hecu")
#     vocabSet.add("absence")
#     vocabSet.add("remove")
#     vocabSet.add("overheated")
#     vocabSet.add("exhoust")
#     vocabSet.add("components")
#     vocabSet.add("component")
#     vocabSet.add("melt")
#     vocabSet.add("illuminates")
#     vocabSet.add("illuminate")
#     vocabSet.add("update")
#     vocabSet.add("updated")
#     vocabSet.add("absorption")
#     vocabSet.add("Tire pressure monitoring systems")
#     vocabSet.add("esc")
#     vocabSet.add("escape")
#     vocabSet.add("escapes")
#     vocabSet.add("upload")
#     vocabSet.add("rescue")
#     vocabSet.add("describing")

    return list(vocabSet)

# 단어별 빈도수 구하기
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def bagOfWords2VecMN_Tot(vocabList, inputSet, totCntList):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
            totCntList[vocabList.index(word)] += 1
    return returnVec

# 나이브 베이지안 
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    print(numTrainDocs, numWords)
#    print(sum(trainCategory))
#    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
#     print(p0Num, len(p0Num))
#     print(p1Num, len(p1Num))
    p0Denom = 2.0; p1Denom = 2.0  
    abus = 0                      #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == "hwt":
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        elif trainCategory[i] == "swt":
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
            abus += 1
        
    pAbusive = abus/float(numTrainDocs)
    
    print(p0Num, len(p0Num))
    print(p0Denom)
    print(p1Num, len(p1Num))
    print(p1Denom)
        
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive,p0Num,p1Num

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
#     p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
#     p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    p1 = sum(vec2Classify * p1Vec) + log(1.0 - pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(pClass1)
    
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
#     vocabList = createVocabList(docList)
    vocabList = whiteVocabList()
    print(vocabList)
    
    trainMat = []; trainClasses = []; totCntList = [0]*len(vocabList)
    for docIndex in range(len(docList)):
        # 등장 빈도 수 체크 vocabList trainMat 같은 인덱스로 묶임!!
        #trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainMat.append(bagOfWords2VecMN_Tot(vocabList, docList[docIndex], totCntList))
        trainClasses.append(docList[docIndex][0])
#        print(trainMat[docIndex])
#         print(trainClasses)
    
    print(totCntList)
    
    # 학습된 테이블
    p0V,p1V,pSpam,p0Num,p1Num = trainNB0((trainMat), (trainClasses))
    
    word_cnt_2014 = open("../2014_word_cnt.txt", "w", encoding='utf8')
    
    for i in range(len(vocabList)):
#         wordCntLine = "%s %d %f %f\n" %(vocabList[i], totCntList[i], p0Num[i], p1Num[i])
        wordCntLine = "%s %d %f %f\n" %(vocabList[i], totCntList[i], p0V[i], p1V[i])
        word_cnt_2014.write(wordCntLine)
#        print(vocabList[i], totCntList[i], p0Num[i], p1Num[i])

    word_cnt_2014.close()
    
    #print(p0V)
    #print(p1V)
    print(pSpam)
    
    # 학습된 테이블 검증
    testDocList=[]; classList = [];
    
    ''' 
    테스트 할 파일  로딩
    '''
#     recall_2014_file_test = open("../new_rcl_out_14.txt", "r", encoding='utf8')
    recall_2014_file_test = open("../FLAT_RCL_Out_15_new.txt", "r", encoding='utf8')
    #recall_2014_file_test = open("../test_set.txt", "r", encoding='utf8')
    for line in recall_2014_file_test:
        line = line.strip()
        wordList = textParse(line)
        testDocList.append(wordList)
    
    error_cnt = 0
    for i in range(len(testDocList)):
        wordVector = bagOfWords2VecMN(vocabList, testDocList[i])
        predic = classifyNB(wordVector,p0V,p1V,pSpam)
        
        kList = ['15e011000', '15v013000', '15v043000', '15v064000', '15v075000']
    
        if testDocList[i][0] in kList:
            print(wordVector)
            
        if predic == "swt":
            error_cnt += 1
            print("SWT Classfication", testDocList[i][0], predic)
#         if testDocList[i][0] != "etc":
#             if predic != testDocList[i][0]:
#                 error_cnt += 1
#                 print ("classification error", testDocList[i][0], predic)
#             else:
#                 print ("classification OK", testDocList[i][0], predic)
             
    print(error_cnt, error_cnt/len(testDocList))
    # print(len(docList))
    # print(vocabList)