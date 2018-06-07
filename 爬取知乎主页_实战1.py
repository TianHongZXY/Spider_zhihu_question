# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from pyquery import PyQuery as pq
import time

def process_url(list,headers):
	length = len(list)
	answer_list=[]
	author_list=[]
	k = 0
	for i in range(1,length,2):
		r = requests.get(list[i],headers=headers)
		doc = pq(r.text)
		if 'zhuanlan' in list[i]:
			answer_items = doc('.Post-RichText').items()
			title = doc('.Post-Title').text()
			author = doc.find('[itemProp=name]').attr('content')
		elif 'question' in list[i]:
			answer_items = doc('.CopyrightRichText-richText').items()
			title = doc('.QuestionHeader-title').text()
			author = doc.find('.UserLink-link').text()
			#author2 = doc.find('.UserLink-link').eq(1).text()
		else:
			continue
			#开始用的列表存问题内容，后来想想直接输出在文件里了，一个标题对一个问题的所有回答items
		'''for answer_item in answer_items:
			#print(answer_item)
			answer = answer_item.text()
			answer_list.append(answer)
			#print(answer)'''
		now_time = time.strftime('%m-%d_%H-%M', time.localtime(time.time()))
		filename = now_time + 'zhihu.txt'
		with open(filename, 'a', encoding='utf-8') as f:
			f.write('问题标题：' + title + '\n')
			f.write('答主：' + author)
			f.write('\n' + '=' * 80 + '\n')
			for answer_item in answer_items:
				f.write(answer_item.text())
				f.write('\n' + '=' * 80 + '\n')

	'''print('answer_list= ',answer_list)
	print(len(answer_list))
	print(list[k])
	k += 2
	print('\n' + '=' * 80 + '\n')
	print(answer_text)
	print('\n' + '='*80 +'\n')
	print(doc)'''

def get_question_url():
	url = 'https://www.zhihu.com'
	headers = {
	           #'Host':'www.zhihu.com',
	           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
	           }
	s = requests.Session()
	r = s.get(url=url,headers=headers)
	doc = pq(r.text)
	items = doc('.ContentItem-title').items()
	question_url_list = []
	question_url_dict = {}
	for item in items:
		#print(item)
		question = item.find('a').text()
		#print(question)
		meta_url = item.find('meta ')
		url = meta_url.attr('content')
		if url == None:
			meta_url = item.find('a')
			url = 'https:' + meta_url.attr('href')
		question_url_list.append(question)
		question_url_list.append(url)


	process_url(question_url_list,headers)
	print(question_url_list)

if __name__ == '__main__':
	while True:
		get_question_url()
		time.sleep(3600)
