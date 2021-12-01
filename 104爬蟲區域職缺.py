from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

df = []

#設定區域查詢值
dics = {"台北市":6001001000,
    "新北市":6001002000,
    "宜蘭縣":6001003000,
    "基隆市":6001004000,
    "桃園市":6001005000,
    "新竹縣市":6001006000,
    "苗栗縣":6001007000,
    "台中市":6001008000,
    "彰化縣":6001010000,
    "南投縣":6001011000,
    "雲林縣":6001012000,
    "嘉義縣市":6001013000,
    "台南市":6001014000,
    "高雄市":6001016000,
    "屏東縣":6001018000,
    "台東縣":6001019000,
    "花蓮縣":6001020000,
    "澎湖縣":6001021000,
    "金門縣":6001022000,
    "連江縣":6001023000,
    "大陸地區":6002000000,
    "其他亞洲":6003000000,
    "大洋洲":6004000000,
    "美加地區":6005000000,
    "中南美洲":6006000000,
    "歐洲":6007000000,
    "非洲":6008000000}

listkey=list(dics.keys())
listvalue=list(dics.values())

for i in range(len(listkey)):
    
    area=listvalue[i]

    #查詢職缺數
    '''
    url = 'https://www.104.com.tw/jobs/search/?ro=0&isnew=30&keyword=' + keyword + \
          '&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&s9=1&page=' + \
          str(page) + '&mode=s&jobsource=2018indexpoc'
    '''
    
    url = 'https://www.104.com.tw/jobs/search/?ro=0&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=' + str(area) + \
         '&order=11&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0'
    driver=webdriver.Chrome()
    driver.get(url)

    '''
    html=requests.get(url)
    html.encoding = 'UTF-8'
    '''
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, "lxml")
    
    #列印地區
    jobarea=listkey[i]
    print(listkey[i])

    for d1 in soup.find_all(id='js-job-tab'):
        #for d2 in d1.attrs.get('data-value="0"'):
        jobs=d1.get_text()
        print(jobs)

    break    
'''        
    #組成表格
    OutputDf = pd.DataFrame({jobarea, 
                             jobs},
                            columns=['地區'],
                            index=['全部','全部2'])
    print(OutputDf)
    break
    time.sleep(3)
'''    
driver.close()