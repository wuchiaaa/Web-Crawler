import requests
from bs4 import BeautifulSoup
import pandas as pd

df = []
baseurl = 'https://www.1111.com.tw/search/job?ks=%E9%9B%BB%E8%85%A6&fs=1&ps=100&page='  # 電腦

# 取得總頁數
html = requests.get(baseurl + '1')
soup = BeautifulSoup(html.text, 'lxml')
tem = soup.find('select', class_="custom-select").text
page = int(tem.replace('1 / ', ''))
if page > 15:   # 最多取15頁資料
    page = 15

# 逐頁讀取資料
for i in range(page):
    url = baseurl + str(i+1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    job = soup.select(".it-md")   # 取 class=it-md 內容
    for j in range(len(job)):
        work = job[j].a.text   # 職務名稱
        site = job[j].a.get('href')   # 工作網址
        company = job[j].find('div', class_='d-none d-md-flex jb-organ').a.text   # 公司名稱
        companysort = job[j].find('div', class_='d-none d-md-flex jb-organ').span.text   # 公司類別
        companysort = companysort.replace('｜','')
        area = job[j].find('span', class_='d-inline d-lg-none').text   # 工作地點
        salary = job[j].find('span', style='color:#dd7926;').text   # 薪資
        experience = job[j].find('span','d-none d-md-inline').text   # 工作經驗
        tem1 = job[j].find('div', class_='text-truncate needs').select('span')  # 學歷
        school = tem1[3].text
        tem2 = job[j].find('div', class_='col-12 jbInfoTxt UnExtension')   # 工作內容
        temlist = tem2.find_all('p')
        content = ''   #工作內容
        for k in range(len(temlist)):
            content += temlist[k].text
        
        # 資料放到pandas
        dfmemo = pd.DataFrame([{'職務名稱': work,
                                '工作網址': site,
                                '公司名稱': company,
                                '公司類別': companysort,
                                '工作地點': area,
                                '薪資': salary,
                                '工作經驗': experience,
                                '學歷': school,
                                '工作內容': content }],
                                )
        # 因顯示的順序與DataFrame定義中的順序不一致，故再次設定cols
        cols = ['職務名稱', '工作網址', '公司名稱', '公司類別', '工作地點', '薪資', '工作經驗', '學歷', '工作內容']
        dfmemo=dfmemo.loc[:, cols]   # DataFrame的行索引不變，列索引是cols中給定的索引值
        
        df.append(dfmemo)
    print('處理第 ' + str(i+1) + ' 頁完畢!')
df = pd.concat(df, ignore_index= True)
df.to_excel('1111data.xlsx', index=0)   # 存為excel檔 

    