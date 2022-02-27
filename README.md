# cosine_similarity
Using cosine similarity equation to compare the closest word in the table

When using voice recognition to capture some specific keyword/word that need to be matched with the word in the predefined table
to find the closest word in the table, sometimes the input word is not exactly match with word in the table causing an error or unrecognised keyword.
We can use this algorithm to find the closest word in the table.


How to find closest word:
1) change the input word and words in the table into 26 dimensional vectors
2) use numpy cosine similarity equation to calculate the similarity
3) find the word with highest similarity 
