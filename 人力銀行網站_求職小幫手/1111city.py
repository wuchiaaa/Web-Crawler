import pandas as pd
import matplotlib.pyplot as plt

'''
 matplotlib.rc    # rc能設置字體與顏色，但電腦裡有的字體不代表 matplotlib 也有
 解決方法：
 import matplotlib
 matplotlib.rc("font",family='Adobe Heiti Std')
 嘗試結果：中文仍無法顯示(換成Pycharm可顯示)
 參考<FontManager.py>
'''


plt.rcParams['font.sans-serif'] = 'Adobe Heiti Std'  # 顯示中文:一般使用Microsoft JhengHei
plt.rcParams['axes.unicode_minus'] = False   # 顯示正負號

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄'] #六都
citycount = []  #六都工作職缺數量
for i in range(len(city)):
    df1 = df[df['工作地點'].str.contains(city[i])]
#    print(len(df1))
    citycount.append(len(df1))
    
ser = pd.Series(citycount, index=city)
print(ser)

# 繪製圖
plt.axis('off')
ser.plot(kind='pie', title='六都電腦職缺數量', figsize=(6,6))