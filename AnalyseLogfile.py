import pandas as pd
import xlwt
apacheLogFile='Apache_log/Apache_2k.log'
dic={'date': [] ,'notice_error':[],'detail':[]}
L=[]
with open(apacheLogFile,'r') as f:
    lines=f.readlines()
    print(lines[0].split('[')[2].split(']')[0])
    for line in lines:
        detail=line.split('[')[2].split(']')

        dic['notice_error'].append(detail[0])
        dic['date'].append(line.split('[')[1].split(']')[0])
        dic['detail'].append(detail[1])

        # df=pd.DataFrame(line,columns=['error','notice'])
    print(dic['notice_error'])

    print(dic['detail'])
    print(dic['date'])
    print(len(dic['date']))
    print(len(dic['notice_error']))
    print(len(dic['detail']))
    pass
df=pd.DataFrame(dic)
print(df)
file='log.xls'
df.to_excel(file)
