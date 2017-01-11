#coding:utf-8

inverted_index = [{'document':{'doc1':1},'query':u'海因裏希'},{'document':{'doc1':1},'query':u'希姆萊'},{'document':{'doc1':1},'query':u'海因裏希'},{'document':{'doc1':1},'query':u'魯'},{'document':{'doc1':1},'query':u'伊特'},{'document':{'doc1':1},'query':u'伯德'},{'document':{'doc1':1},'query':u'希姆萊'},{'document':{'doc2':1},'query':u'是'},{'document':{'doc2':1},'query':u'一個'},{'document':{'doc2':1},'query':u'由'},{'document':{'doc2':1},'query':u'主權國家'},{'document':{'doc2':1},'query':u'組成'},{'document':{'doc2':1},'query':u'的'},{'document':{'doc2':1},'query':u'國際'},{'document':{'doc2':1},'query':u'組織'},{'document':{'doc3':1},'query':u'海因裏希'},{'document':{'doc3':1},},{'document':{'doc3':1},'query':u'主權國家'},{'document':{'doc3':1},'query':u'組成'},{'document':{'doc3':1},'query':u'的'},{'document':{'doc3':1},'query':u'魯'},{'document':{'doc3':1},'query':u'伊特'}]

if any(i['query'] == u'海因裏希' for i in inverted_index):
	if any(i['document'].get('doc1',False) for i in inverted_index):
		print inverted_index[inverted_index.index(index for index in inverted_index if any(i['query'] == u'海因裏希' for i in inverted_index)).next()]['document']['doc1']