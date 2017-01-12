from math import log
DOC_NUM = 20

def tf(word,doc_id):
	return word[doc_id]

def idf(word):
	total = 0
	for k,v in word.iteritems():
		total +=v
	return float(total/DOC_NUM)
def tf_idf(word,doc_id):
	return tf(word,doc_id)*idf(word)
