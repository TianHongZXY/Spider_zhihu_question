# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from pyquery import PyQuery as pq
import time

def process_url(list,headers):
	length = len(list)
	#print(length)
	answer_list=[]
	author_list=[]
	k = 0
	for i in range(1,length,2):
		#print('i= ',i)
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
		#auth_num = 0
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
	print('\n' + '='*80 +'\n')'''

	#print(doc)

def get_question_url():
	url = 'https://www.zhihu.com'
	headers = {
	           #'Host':'www.zhihu.com',
	           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
	           'cookie':'tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; _xsrf=73a2f9f5-53cb-45dd-86a4-584001dc7086; d_c0="AOBkxmhXtQ2PThugKe3zGTMFFZuWsJGa7oY=|1528287917"; q_c1=8d818997bdb44ec0a08f5ef96d598ee4|1528287917000|1528287917000; _zap=9ec75443-cf6a-44b9-bbdf-17909157bd29; capsion_ticket="2|1:0|10:1528287923|14:capsion_ticket|44:MTFkMTJiNTUzNGU0NDdiNjlhODc3YjJhODdmNWVkNGY=|c282283153ff8af9004d0f5b47580226487b4cabe1690cf58924ca50c3f2be4c"; z_c0="2|1:0|10:1528287928|4:z_c0|92:Mi4xeG1taEJnQUFBQUFBNEdUR2FGZTFEU1lBQUFCZ0FsVk51Q0FGWEFCT0paM0dFMHNjdDZxNVNWWGFSSndZbjVKQ2RR|66027bf584ee52ef4bb242c1819848143638c3e225b2842f7792a685eb61af35"'
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
