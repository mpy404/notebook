import requests
from lxml import etree 
# etree = lxml.html.etree
# https://ibaotu.com/sy/17-92085-0-0-0-1.html
class a(object):
    def s_re(self):
        for i in range(1,10):
            print("==========正在爬取第%s页========="%i)
            response = requests.get("https://ibaotu.com/shipin/7-0-0-0-0-" + str(i) + ".html")
            html = etree.HTML(response.content.decode())
            self.x_d(html)
    
    def x_d(self,html):
        s_list = html.xpath('//div[@class="video-play"]/video/@src')
        t_list = html.xpath('//span[@class="video-title"]/text()')
        for s , t in zip(s_list,t_list):
            url = "http:" + s
            name = t + ".mp4"
            response = requests.get(url)
            print()
            with open(name,"wb") as f:
                f.write(response.content)

a = a()
a.s_re() 
