import pandas as pd 
import requests as re
import json
import time

def Super():
	test = True
	while test:
		try:
			data = re.get("https://production.api.coindesk.com/v2/exchange-rates", headers={'Cache-Control': 'no-cache'})
			dic = data.text
			dic = json.loads(dic)
			test = False
		except:
			pass
	di= dic['data']
	d = di["ZMW"]
	d = d['rate']
	return d




def Zmk():
	test = True
	data = re.get("https://secure.zanaco.co.zm/vsuite/vnet/web-banking/public/exchangeRates/get", headers={'Cache-Control': 'no-cache'})
	dic = data.text
	dic = json.loads(dic)
	di= dic['data']
	currency = True
	while currency:
		for i in range(len(di)):
			if di[i]['currencyCode'] == 'USD':
				return {"Buying":di[i]['buyRate'],"Mid":di[i]["midRate"],"Selling":di[i]["sellRate"]} 
	



def Crypto(currency):
	data = re.get("https://production.api.coindesk.com/v2/tb/price/ticker?assets=BTC,ETH,XRP,BCH,EOS,XLM,LTC,ADA,XMR,DASH,IOTA,TRX,NEO,ETC,XEM,ZEC,BTG,LSK,QTUM,BSV,DOGE,DCR,USDT,USDC,LINK,XTZ,ZRX,DAI,BAT,OXT,ALGO,ATOM,KNC,OMG,ANT,REP,BAND,BTT,MANA,FET,ICX,KAVA,LRC,MKR,MLN,NANO,NMR,PAXG,USDP,SC,STORJ,WAVES,FIL,CVC,DNT,REN,BNT,WBTC,GRT,UNI,DOT,YFI,AAVE,NU,MATIC,AMP,CELO,COMP,CRV,RLC,KSM,NKN,SHIB,SKL,SNX,LUNC,UMA,ICP,SOL,AVAX,UST,ENJ,IOTX,AXS,XYO,SUSHI,ANKR,CHZ,LPT,COTI,KEEP,SAND,GALA,APE,CRO,ACHP,JASMY,REQ,SLP,NEAR,MBOX,POLIS,MOVR,POLS,QUICK,MINA,IMX,XEC,NEXO,RUNE,QNT,VET,CAKE,BNB,THETA,HBAR,FTM,RVN,ZIL,DGB,FTT,ENS,WRX,WAXP,EGLD,BUSD,CEL,OP,LUNA,RAY,FLOW,AUDIO,ROSE,CKB,VGX,YGG,CHR,STMX,SXP,INJ,JOE,POLY,STX,SFP,FARM,XVG,CLV,WOO,GLMR,STEEM,RARE,IDEX,SRM,PYR,MIR,SYS,ALPACA,QSP,SCRT,SUN,APT,MASK,DYDX,LDO,CVX,GMT,CTSI,METIS,FORTH,RBN,SAMO,SPELL,ARB,BLUR,GAS,RACA,BABYDOGE,FLOKI,HOT,BFC,KISHU,ELON,SAITAMA,REEF,CEEK,ATLAS,LOOKS,WIN,ONE,DENT,GST,TWT,HNT,AGLD,BTRST,ETHW,ILV,RARI,STG,SYN,TOKE,BLZ,FLR,FIS,GNS,ID,PEPE,SNGLS", headers={'Cache-Control': 'no-cache'})
	dic = data.text
	dic = json.loads(dic)
	di= dic['data']
	try:
		name = di[f'{currency}']['name']
		per = di[f'{currency}']['change']['percent']
		value = di[f'{currency}']['change']['value']
		over = di[f'{currency}']['ohlc']['o']
		high = di[f'{currency}']['ohlc']['h']
		low = di[f'{currency}']['ohlc']['l']
		current = di[f'{currency}']['ohlc']['c']
		circulatingSupply = di[f'{currency}']['circulatingSupply']
	except:
		print(f'Wrong input, Select from this keys {di.keys()}')
		return None,None,None,None,None,None,None
	return name,per,value,over,high,low,current,circulatingSupply

def Pricing():
	#Collecting the data on BTC and ETH 
	name = []
	per = []
	value = []
	over = []
	high = []
	low = []
	current = []
	circulatingSupply = []
	crypto = ['BTC',"USDC",'ETH']
	q = 0
	for i in range(len(crypto)):
		getting = True
		while getting:
			try:
				namex,perx,valuex,overx,highx,lowx,currentx,circulatingSupplyx = Crypto(crypto[i])
				q = 0
				getting = False
			except:
				q+=1
				if q >= 200:
					getting = False
					break
		name.append(namex)
		per.append(perx)
		value.append(valuex)
		over.append(overx)
		high.append(highx)
		low.append(lowx)
		current.append(currentx)
		circulatingSupply.append(circulatingSupplyx)
 
	Zed = round(Super(),2)
	l1= Zed * current[0]
	l2= Zed * current[1]
	l3= Zed * current[2]
	print(Zed)
	time.sleep(60*30)
	q = 0

	#Comparing Data Of BTC and ETH after 5 min
	getting = True
	
	while getting:
		try:
			n,new,v,o,h,l,cu1,c = Crypto(crypto[0])
			n,new2,v,o,h,l,cu2,c = Crypto(crypto[1])
			n,new3,v,o,h,l,cu3,c = Crypto(crypto[2])
			getting = False
			Zed = round(Super(),2)
			l4= Zed * cu1
			l5= Zed * cu2
			l6= Zed * cu3
		except:
			q+=1
			if q > 500:
				getting = False
				break

	Buy = []
	Buy1 = []
	if l4 -l1 > 50:
		Buy1.append('Buy N Sell Later')
		Buy.xcappend(f"Gains K: {l4 -l1}")
	elif l1 -l4 > 50:
		Buy1.append('Sell N Buy Later')
		Buy.append(f"Sell K:{l1 -l4}")
	else:
		Buy1.append("Keep")
		Buy.append("Keep")

	if l5 -l2 > 50:
		Buy1.append('Buy N Sell Later')
		Buy.append(f"Gains K: {l5 -l2}")

	elif l2 -l5 > 50:
		Buy1.append('Sell N Buy Later')
		Buy.append(f"Sell K:{l2 -l5}")

	else:
		Buy1.append("Keep")
		Buy.append("Keep")


	if l6 -l3 > 50:
		Buy1.append('Buy N Sell Later')
		Buy.append(f"Gains K: {l6 -l3}")

	elif l3 -l6 > 50:
		Buy1.append('Sell N Buy Later')
		Buy.append(f"Sell K:{l3 -l6}")

	else:
		Buy1.append("Keep")
		Buy.append("Keep")

	dic = {
		"name":name,
		"percent":per,
		"Value":value,
		"Over":over,
		"High":high,
		"low":low,
		"Current_Price":current,
		"circulatingSupply":circulatingSupply,
		"Gain/Loss":Buy1
	}
	print(Buy)
	return dic

q = 0
while q< 20:
	pd.set_option('display.max_columns', None)
	pd.set_option('display.max_rows', None)
	df = pd.DataFrame(Pricing())

	print("*************************************************************************************")
	print(df)
	q+=1
	
	df.to_csv('cryptodata.csv',mode='a', index=False, header=False)
	print("*************************************************************************************")
	# print(Zmk())




