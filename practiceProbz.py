#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:02:40 2019

@author: alicenguyen
"""
def returnTf(self, query, dID, D1, D):
    tf1 = 0
    tf2 = 0
    listPTR = list();
    if query in D1:
        listPTR = D1[query]
        for pair in listPTR:
            if pair[0] == dID:
                tf1 = pair[1]
        for docId, wordCount in D.items():
            if dID == docId:
                tf2 = wordCount
    if tf2 != 0:
        #print(tf2)
        tf = tf1/tf2 
    else:
        tf = 0
    return tf

import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

filepath = "data/ap89_collection";
paraHolder = "";
docIdHolder = "";
textHolder = "";
 ##listTextHolder = list();
D1 = dict()
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

sentence = ""
ps = PorterStemmer()

Stop = list();
filepath = 'stoplist.txt';
with open(filepath) as f:
    for line in f:
        for word in line.split():
            Stop.append(word)

for i, txt in D1.items():
    sentence = txt
    words = word_tokenize(sentence)
    sentence = ""
    for w in words:
        w = w.lower()
        if w not in Stop:
            sentence = sentence + " " + ps.stem(w)
    D1[i] = sentence

count = 0;
DocCountInd = dict()
DocCountInd2 = dict()
wCountHolder = 0
ListPTR = list()
for i, sen in D1.items():
    for word in sen.split():
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
   
Q1 = dict()
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
                print(textHolder)
                textHolder = textHolder.rstrip('.')
                Qnumber = int(textHolder)
                textHolder = ""
            else:
                textHolder = textHolder + " " + word
        Q1[Qnumber] = textHolder
        textHolder = ""
        firstWinLine = 0


    

    