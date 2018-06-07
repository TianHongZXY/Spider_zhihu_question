import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/explore'
headers = {
	'User-Agent':'Mozilla/5.0',
	#'cookies':'d_c0="AOBjyjaepg2PTs1alB4-1obPMOo6QoUJEZQ=|1527299845"; q_c1=0f318948cb6444148871f47d0763a8d6|1527299845000|1527299845000; _zap=dd3c6571-34e4-4792-aa7d-29b506ca7de8; capsion_ticket="2|1:0|10:1527299921|14:capsion_ticket|44:NzY0OTVhZDAyYWNkNGFkZWFmY2I2YzU3YjgyMzM4ODg=|863cbad546f90a43e7cbc3650ffc2645ed81267b4e7aa865ca00d9ebf9ee4c7c"; z_c0="2|1:0|10:1527299927|4:z_c0|92:Mi4xeG1taEJnQUFBQUFBNEdQS05wNm1EU1lBQUFCZ0FsVk5WdzMyV3dETWdxaG1iR3cxbXdtTmNDZm83eVE4b3R5Q3lR|9c9f0566bd08a1820ee154166ec061bde729535362d9f658c4eb0f53e18e75a0"; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; _xsrf=034c3ad3891d516a3e68dae01217a389; __utma=51854390.987028371.1528210741.1528210741.1528210741.1; __utmb=51854390.0.10.1528210741; __utmc=51854390; __utmz=51854390.1528210741.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20171124=1^3=entry_date=20171124=1'
}
html = requests.get(url, headers=headers).text
#soup = BeautifulSoup(html)
#print(soup.prettify())
#print(html.status_code)
doc = pq(html)
print(type(doc))
items = doc('.explore-tab .feed-item').items()
print(items)
for item in items:
	#print(item)
	question = item.find('.question_link').text()
	author = item.find('.author-link-line').text()
	answer = pq(item.find('.content').html()).text()
	with open('explore4.txt','a',encoding='utf-8') as f:
		f.write('\n分割\n'.join([question,author,answer]))
		f.write('\n' + '=' * 80 + '\n')