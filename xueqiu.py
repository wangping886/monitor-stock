import json
import pysnowball as ball


def getPriceList(codes,dataMap):
    #循环数组
    for index,code in enumerate(codes):
        if index==0:###############
            symbol=code
        else:
            symbol=symbol+'&symbol='+code
    
    print(f'==={symbol}==={codes}')

    for data in ball.quotec(symbol)['data']:
        stock_name = dataMap.get(data['symbol'], '未知股票')
        # 获取股票涨幅
        percent = data['percent']
        low =(data['low']-data['last_close'])*100/data['last_close']
        low=round(low, 2) #保留两位
        high =(data['high']-data['last_close'])*100/data['last_close']
        high=round(high, 2) #保留两位
        # 格式化输出股票名称和股票价格
        print(f'{stock_name} 的涨幅是: {percent},最低点位：{low},最高点位：{high}')

        
ball.set_token("xq_a_token=e9373e1b65ec0f1e6706060d6d5cfca055a5e3fd")

#print(json.dumps(ball.quotec('SH600000'), indent=4))#获取某支股票的行情数据

quanzhongMap = {'SH601166':'兴业银行','SH600900':'长江电力',#A50权重
'SH688981': '中芯国际','SH688256': '寒武纪',#科创权重
'SZ300750': '宁德时代','SH601398': '工商银行',#创业权重
}
quanzhongCodes = list(quanzhongMap.keys())

cosumeMap={'SH600809':'山西汾酒','SH600132':'重庆啤酒','SZ002475':'立讯精密','SZ002384':'东山精密'}
cosumeCodes = list(cosumeMap.keys())

aiMap={'SZ300308':'中际旭创','SZ300502':'新易盛','SZ002463':'沪电股份','SZ000063':'中兴通讯','SH600567':'山鹰国际','SH600498':'烽火通信'}
aiCodes = list(aiMap.keys())

fundMap ={ 'SH588000': '科创50ETF','SH510050': 'A50ETF', 'SH510300': '沪深300','SZ159915':'创业板ETF'}
fundCodes = list(fundMap.keys())

getPriceList(quanzhongCodes,quanzhongMap)
getPriceList(cosumeCodes,cosumeMap)
getPriceList(fundCodes,fundMap)
getPriceList(aiCodes,aiMap)



# #利润表
# print(json.dumps(print(ball.income(symbol='SZ300251',is_annals=1,count=10)) , indent=4))
# #主营业务构成
# print(json.dumps(ball.business(symbol='SZ300251',count=10), indent=4))


#print(ball.convertible_bond(page_size=5, page_count=1)) #可转债
# ball.index_perf_7("399967") #最近7天数据
# ball.index_perf_30("399967") #最近30天数据
# ball.index_perf_90("399967") #最近90天数据

# print(ball.fund_detail("008975")) 基金详情
