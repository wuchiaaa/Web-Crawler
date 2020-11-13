import pandas as pd
import matplotlib.pyplot as plt
import xlrd

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'  # 顯示中文
plt.rcParams['axes.unicode_minus'] = False  # 顯示正負號

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  # 六都
citycount = []  # 六都工作職缺數量
for i in range(len(city)):
    df1 = df[df['工作地點'].str.contains(city[i])]
    #    print(len(df1))
    citycount.append(len(df1))

ser = pd.Series(citycount, index=city)
print(ser)

# plt.axis('off')
# ser.plot(kind='pie', title='六都電腦職缺數量', figsize=(6, 6))
plt.figure(figsize=(6, 6))
plt.title('六都電腦職缺數量')
plt.pie(ser, labels=city)

plt.show()
