#-*-coding:utf-8-*-

import os
import subprocess
import requests
import time
#import re
from bs4 import BeautifulSoup

requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数

headers = {'User-Agent': 'my custom user agent', 'Cookie': 'haha','Connection': 'close',}
 
if __name__ == '__main__':

    
    #  网站根网址
    root_url = 'http://www.ccgp-jiangsu.gov.cn/ggxx/zbgg/shengji/'
    #  保存本地路径
    path = 'raw.txt'
    f=open(path,"w",encoding='utf-8')

    for page in range(0,28):
        # time.sleep(3)
        if page==0:
            # 要下载的网页
            url = 'http://www.ccgp-jiangsu.gov.cn/ggxx/zbgg/shengji/'
        else:
            url = 'http://www.ccgp-jiangsu.gov.cn/ggxx/zbgg/shengji/index_'+str(page)+'.html'
            print(url)
        
        # 解析网址
        req = requests.get(url)
        # re = requests.session()
        # re.keep_alive = False
        # time.sleep(2)
        # 设置编码，浏览器查看网站编码：F12，控制开输入document.characterSet回车即可查看
        req.encoding = 'utf-8'
        
        
        # 获取网页所有内容
        soup = BeautifulSoup(req.text, 'html.parser')
        
        
        # 查找网页中ul的内容
        list_tag = soup.findAll("ul")
      
    
        # 查看ul中li标签的内容
        li = list_tag[0](['li'])
        print(li)
        # 循环遍历
        
        for i in li:
            # 获取到a标签间的内容---标题
            txt_type = i.a.string
            
            # 获取a标签的href地址值---网址
            short_url = (i(['a'])[0].get('href'))
     
            # 获取网页设置网页编码
            req = requests.get(root_url + short_url)
            # re = requests.session()
            # re.keep_alive = False
            # time.sleep(1)
            req.encoding = 'utf-8'
     
            # 解析网页
            soup = BeautifulSoup(req.text, "html.parser")
            
            f.write('\n')
            f.write(root_url+short_url)
            for p in soup.select('p'):
                text=p.get_text()
                #f.write('第'+str(j)+'页')
                f.write('\n')
                f.write(text)
                f.write('\n')
            # f.close
    f.close
subprocess.call([os.getcwd()+'/test.out', '99'])