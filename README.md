# Information-Retrieval-Cos-Sim
## Overview
This program runs the queries in query_list.txt with 73 documents in ap89_collection. A results files contains the 
"QueryNumber Q0 docNumber rankOfSimilarity score EXP"
## StemmingAndStopping
The parsing will take in relevant information from both query_list.txt and ap89_collection, excluding stopwords and 
## Getting TF IDF
The queries and documents are parsed and put into respective dictionaries and placed into a class (CollectionOfFiles) which
will calculate the indexes. There will be functions in this class which will return TF and IDF values if word searched for
and documend ID is entered.
## Getting Cos Similarity
Using the TF and IDF functions Cos Similarity is calculated as follows:</br>
* Query = {"bob", "burger"}, Document = {"bob", "bam", "burger"} </br>
CosSim = <tf "bob" from Q> * <tf "bob" from D> * <idf "bob" from Q> + <tf "burger" from Q> * <tf "burger" from D> * <idf "burger" from Q> </br>
divided by </br>
squareRoot(<tf "bob" from Q>^2 + <tf "burger" from Q>^2)*(<tf "bob" from D>^2 + <tf "burger" from D>^2) ) </br>
  The closer the CosSim is to 1, the more similar the document and query is.
## Results
The results from CosSimilarity are listed in results_file.txt. The results will be in this form "QueryNumber Q0 docNumber rankOfSimilarity score EXP" </br>
  {QueryNumber} will indicate which Query is being compared. </br>
  {docNumber} will indicate which Document is being compared. </br>
  {rankOfSimilarity} is a number ranking how close the document is to the query compared to the other documents in the
    collection; 1 will be most similar, 100 will be the least similar </br>
  {score} is the cosine similarity score of the document and query </br>
