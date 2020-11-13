import pandas as pd
import re
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  # 六都
salarylist = []  # 六都薪水
for i in range(len(city)):
    df1 = df[(df['工作地點'].str.contains(city[i])) & (df['薪資'].str.contains('月薪'))]
    indexlist = df1.index  # 資料索引
    #    print(len(df1))
    total = 0  # 薪資總額
    for j in range(len(df1)):
        salarytem = df1['薪資'][indexlist[j]].replace(',', '')
        salarynum = re.findall(r"\d+\.?\d*", salarytem)
        if len(salarynum) == 1:  # 單一薪資或以上
            salary = int(salarynum[0])
        else:  # 兩個薪資則取平均數
            salary = (int(salarynum[0]) + int(salarynum[1])) / 2
        total += salary
    salarycity = int(total / len(df1))  # 六都平均薪資
    salarylist.append(salarycity)

# print(salarylist)
ser = pd.Series(salarylist, index=city)
print(ser)

# 繪製圖
plt.figure(figsize=(6, 6))
plt.title('六都電腦職缺薪資')
plt.bar(ser.index, ser.values)
plt.ylabel('單位：元')

plt.show()