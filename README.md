# Information-Retrieval-Cos-Sim
## Overview
This program runs the queries in query_list.txt with 73 documents in ap89_collection. A results files contains the 
"<Query Number> Q0 <doc number> <rank of similarity> <score>"
## Getting TF IDF
The queries and documents are parsed and put into respective dictionaries and placed into a class (CollectionOfFiles) which
will calculate the indexes. There will be functions in this class which will return TF and IDF values if word searched for
and documend ID is entered.
## Part 2
Part two contains three python files. 
* IndexA.py <br />
IndexA program will read in the txt files in data folder and create an index which keeps track of the frequency of every word in each file, excluding stop words. When you run the indexA file, it will automatically display the index in console. For each word in the collection, it will display the word, then doc number with the frequency in each doc number in pairs. If a doc number is not listed, the word does not occur in the doc. An example is as follows: <br />
WORD -----> disciplines <br />
pair:  20 1 <br />
pair:  17 2  
* IndexB.py <br />
Index B program will read in the txt file in data folder and create an index which keeps track of how many words there are in each file, excluding stop words. When you run the indexB file, it will automatically display the index in console. For each document number, there is a number to track how many words appears in it. An example is as follows: <br />
1 369 <br />
* tfidf.py <br />
tfidf file program will make the indexes above and use them to calculate tf, idf, and tf-idf weights. The program will prompt the user to enter a search word. Then if the search word is in the collection, it will generate a posting of tf, idf, tf-idf weights for the term in each document even if some weights are 0. The user needs to enter 'QUIT' for the loop to stop. An example for the postings of document 2 is as follows: </br>
In document 2 the weights are: </br>
The tf weight for word is:  0.3333333333333333 </br>
The idf weight for word is:  1.584962500721156 </br>
The tf-idf weight for word is:  0.5283208335737186 
