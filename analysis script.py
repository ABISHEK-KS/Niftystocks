import pandas as pd
import statistics
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas_profiling as pp
import mplfinance as mpf

myfile=pd.read_csv('Combined.csv')
df=pd.DataFrame(myfile)
print(df.head())
a=sorted(set(df['Symbol']))

symbolval=0
volsum=[]
opensum=[]
highsum=[]
lowsum=[]
closesum=[]
datelist=[]
summarydataframe=pd.DataFrame()
fulllist=[]
changestats=[]

for j in range(235192):
    Symbol=a[symbolval]
    
    
    if df['Symbol'][j]!=Symbol: 
        volchange=volsum[0]-volsum[-1]
        openchange=opensum[0]-opensum[-1]
        y=[Symbol,volchange,openchange,datelist[0],datelist[-1]]
        changestats.append(y)
        x=[Symbol,datelist[0],datelist[-1],statistics.mean(highsum),statistics.mean(lowsum),statistics.mean(opensum),statistics.mean(closesum),statistics.mean(volsum)]
        
        print('Stock named ',Symbol,'has shown an average high mean of',statistics.mean(highsum),', average low mean of statistics.mean(lowsum)',',average open mean of ',statistics.mean(opensum),',average mean of close ',statistics.mean(closesum),', and an average volume of', statistics.mean(volsum))
        fulllist.append(x)
        volsum=[]
        highsum=[]
        lowsum=[]
        opensum=[]
        closesum=[]
        datelist=[]
        symbolval+=1
        
    else: 
        volsum.append(df['Volume'][j])
        datelist.append(df['Date'][j])
        
        opensum.append(df['Open'][j])
        highsum.append(df['High'][j])
        lowsum.append(df['Low'][j])
        closesum.append(df['Close'][j])
summarydataframe=pd.DataFrame(fulllist,columns=['Stock','Firstdate','LastDate','High','Low','Open','Close','Volume'])
changestatsdf=pd.DataFrame(changestats)
changestatsdf.to_excel('Changestats.xlsx')
summarydataframe.to_excel('SummarySheet.xlsx')

profrep=pp.ProfileReport(myfile)
profrep.to_file('index.html')


   






