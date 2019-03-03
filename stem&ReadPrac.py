#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:22:54 2019

@author: alicenguyen
"""
import nltk
import math
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

class CollectionOfFiles:
    def __init__(self, FileDict):
        #self.FileDict = FileDict
        count = 0;
        DocCountInd = dict()
        DocCountInd2 = dict()
        wCountHolder = 0
        ListPTR = list()
        for i, txt in FileDict.items():
            for word in txt.split():
                count += 1
                if word not in DocCountInd2:
                    ListPTR = [[i, 1]]
                    DocCountInd2[word] = ListPTR
                else:
                    ListPTR = DocCountInd2[word]
                    for pair in ListPTR:
                        if pair[0] == i:
                            wCountHolder = pair[1];
                            wCountHolder += 1;
                            pair[1] = wCountHolder;
                    if wCountHolder == 0:
                        ListPTR.append([i, 1]);
                    DocCountInd2[word] = ListPTR;
                    wCountHolder = 0;
            DocCountInd[i] = count
            count = 0
        self.DocCountInd = DocCountInd
        self.DocCountInd2 = DocCountInd2
        self.FileDict = FileDict
    def printColl(self):
        for i, sen in self.FileDict.items():
            print(i)
            print(sen)
            print("\n\n")
                
    def returnTf(self, query, dID):
        tf1 = 0
        tf2 = 0
        listPTR = list();
        if query in self.DocCountInd2:
            listPTR = self.DocCountInd2[query]
            for pair in listPTR:
                if pair[0] == dID:
                    tf1 = pair[1]
            for docId, wordCount in self.DocCountInd.items():
                if dID == docId:
                    tf2 = wordCount
        if tf2 != 0:
            tf = tf1/tf2 
        else:
            tf = 0
        return tf

    def returnIDF(self, query):
        n = 0
        df = 0;
        listPTR = list();
        if query in self.DocCountInd2:
            listPTR = self.DocCountInd2[query]
            df = len(listPTR)
        n = len(self.DocCountInd)
        if df != 0:
            idf = math.log2(n/df)
        else:
            idf = 0
        return idf
    
    def returnIDlist(self):
        ExList = list()
        for Did, Text in self.DocCountInd.items():
            ExList.append(Did)
        return ExList
    
def parseFileByText(D1):
    filepath = "data/ap89_collection";
    paraHolder = "";
    docIdHolder = "";
    textHolder = "";
    ##listTextHolder = list();
    inId = 0;
    inText = 0;
    with open(filepath) as f:
        for line in f:  
            for word in line.split():
                if inId == 1:
                    docIdHolder = word
                    inId = 0
                if inText == 1:
                    if(word != "</TEXT>"):
                        textHolder = textHolder + " " + word
                    else:
                        paraHolder = paraHolder + textHolder;
                        textHolder = ""
                        inText =  0
                if(word == "</DOC>"):
                    D1[docIdHolder] = paraHolder
                    paraHolder = "";

                if word == "<DOCNO>":
                    inId = 1;
                if word == "<TEXT>":
                    inText = 1;
    return

def StopAndStem(Stop, D1):
    sentence = ""
    ps = PorterStemmer()

    for i, txt in D1.items():
        sentence = txt
        words = word_tokenize(sentence)
        sentence = ""
        for w in words :
            w = w.lower()
            if w not in Stop and w.isprintable() == True:
                sentence = sentence + " " + ps.stem(w)
        D1[i] = sentence
    return 

def parseQueries(Q1):
    filepath = "data/query_list.txt";
    textHolder = "";
    ##listTextHolder = list();
    firstWinLine = 0
    Qnumber = 0
    with open(filepath) as f:
        for line in f:
            for word in line.split():
                if firstWinLine == 0:
                    firstWinLine = 1
                    textHolder = word
                    textHolder = textHolder.rstrip('.')
                    Qnumber = int(textHolder) 
                    textHolder = ""
                else:
                    textHolder = textHolder + " " + word
            Q1[Qnumber] = textHolder
            textHolder = ""
            firstWinLine = 0
    return

def main():
    D1_textFiles = dict()
    #function takes in dictionary and return each document name with coresponding text
    #in D1_textFiles
    parseFileByText(D1_textFiles)
    
    #make list of stopwords to pass into StopAndStem function
    stopWords = list();
    filepath = 'stoplist.txt'
    with open(filepath) as f:
        for line in f:
            for word in line.split():
                stopWords.append(word)
    
    StopAndStem(stopWords, D1_textFiles)
    
    #Collection of Data files, grab TF and IDF values possible with class functions
    CF1 = CollectionOfFiles(D1_textFiles)
    
    Q1_textFiles = dict()
    
    parseQueries(Q1_textFiles)
    
    StopAndStem(stopWords, Q1_textFiles)
    
    #Collection of Data files, grab TF values with class functions
    QF1 = CollectionOfFiles(Q1_textFiles)
    
    RDict = dict() 
    
    '''idfDholder = CF1.returnIDF("discuss", "AP890101-0003")
    print(idfDholder)'''
    
    Didnames = CF1.returnIDlist()
    
    CosTop = 0
    CosBot1 = 0
    CosBot2 = 0
    tfQholder = 0
    tfDholder = 0
    idfDholder = 0
    holder = 0 
    cos = 0
    
    f=open("results_file.txt", "a+")
    
    for Qnum, Q in Q1_textFiles.items():
        for counter in range(73):
            for word in Q.split():
                tfQholder = QF1.returnTf(word, Qnum)
                tfDholder = CF1.returnTf(word, Didnames[counter])
                idfDholder = CF1.returnIDF(word)
                holder = tfQholder*tfDholder*idfDholder
                CosTop = CosTop + holder
                holder = (tfDholder*idfDholder)**2
                CosBot1 = CosBot1 + holder
                holder = tfQholder**2
                CosBot2 = CosBot2 + holder
            if CosBot1 == 0:
                cos = 0
            else:
                cos = CosTop/(math.sqrt(CosBot1*CosBot2))
            holder = 1+counter
            RDict[Didnames[counter]] = cos
            CosTop = 0
            CosBot1 = 0
            CosBot2 = 0
        sortedDocs = sorted(RDict, key = RDict.get, reverse=True)
        holder = 0
        for s in sortedDocs:
            holder += 1
            f.write(str(Qnum))
            f.write(" Q0 ")
            f.write(s)
            f.write(" ")
            f.write(str(holder))
            f.write(" ")
            if RDict[s] == 0:
                f.write("0 ")
            else:
                f.write(str(RDict[s]))
            f.write(" EXP \n")
    f.close()
            
main()
