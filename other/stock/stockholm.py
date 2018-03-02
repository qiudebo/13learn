
import argparse
import option

import csv
import os
import datetime
import json
import re
import io

import requests


import timeit
import time

from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

import pandas as pd
from pandas.io.excel import ExcelFile
import codecs

class Stockholm(object):

	def __init__(self,args):
		self.reload_data=args.reload_data
		self.gen_portfolio = args.gen_portfolio
		self.output_type=args.output_type
		self.charset=args.charset
		self.test_date_range=args.test_date_range
		self.start_date=args.start_date
		self.end_date=args.end_date
		self.target_date=args.target_date
		self.thread=args.thread
		if(args.store_path=='./tmp/stockholm_export'):
			self.export_folder=os.path.expanduser('~')+'/tmp/stockholm_export'
		else:
			self.export_folder=args.export_folder
		self.testfile_path=args.testfile_path
		self.methods=args.methods
		self.all_quotes_url='http://money.finance.sina.com.cn/d/api/openapi_proxy.php'
		
		self.export_file_name = 'stockholm_export'
		self.index_array=['000001.SS','399001.SZ','000300.SS']
		self.sh000001={'Symbol':'000001.SS','Name':u'上证指数'}
		self.sz399001={'Symbol':'399001.SS','Name':u'深证指数'}
		self.sh000300={'Symbol':'399005.SZ','Name':u'中小板指数'}

	def data_load(self,start_date,end_date,output_types):
		all_quotes=self.load_all_quote_symbol()
		code=[]
		name=[]
		for quote in all_quotes:
			code.append(quote['Symbol'])
			name.append(quote['Name'])
		df=pd.DataFrame(list(zip(code,name)),columns=['symbol','name'])
		df.to_csv("./shsz.csv", encoding='utf_8_sig')

		# for quotes in all_quotes:
		# 	print(quotes)
		#self.load_all_quote_data(all_quotes,start_date,end_date)
		#self.data_export(all_quotes,output_types,None)
		print(str("total "+str(len(all_quotes)))+" quotes are loaded"+"\n")

	def load_all_quote_symbol(self):
		print("loading all quotes sysmbol start..."+"\n")
		start = timeit.default_timer()
		all_quotes=[]
		all_quotes.append(self.sh000001)
		all_quotes.append(self.sz399001)
		all_quotes.append(self.sh000300)
		try:
			count=1
			while(count<100):
				para_val='[["hq","hs_a","",0,'+str(count)+',500]]'
				r_params={'__s':para_val}
				r=requests.get(self.all_quotes_url,params=r_params)
				if(len(r.json()[0]['items'])==0):
					break
				for item in r.json()[0]['items']:
					quote={}
					code=item[0]
					name=item[2]
					# if(code.find('sh')>-1):
					# 	code=code[2:]+'.SS'
					# elif(code.find('sz')>-1):
					# 	code=code[2:]+'.SZ'
					quote['Symbol']=code
					quote['Name']=name
					all_quotes.append(quote)
				count+=1
		except Exception as e:
			print("Error:Failed to load all stock symbol..."+"\n")
			print(e)
		print("load_all_quote_symbol end ... time cost"+str(round(timeit.default_timer()-start))+"s"+"\n")
		return all_quotes

	def load_all_quote_data(self,all_quotes,start_date,end_date):
		print("load_all_quote_data start ..." + "\n")
		start = timeit.default_timer()
		counter = []
		mapfunc = partial(self.load_quote_data,start_date=start_date,end_date=end_date,is_retry=False,counter=counter)
		pool=ThreadPool(self.thread)
		pool.map(mapfunc,all_quotes)
		pool.close()
		pool.join()
		print("load_all_quote_data end ... time cost "+str(round(timeit.default_timer()-start))+"s"+"\n")
		return all_quotes

	def load_quote_data(self,quote,start_date,end_date,is_retry,counter):
		print("load_quote_date begin ..."+"\n")
		start = timeit.default_timer()
		if(quote is not None and quote['Symbol'] is not None):
			try:
				url='http://data.gtimg.cn/flashdata/hushen/latest/daily/' + quote['Symbol'] + '.js'
				r=requests.get(url)
				print(r.url)

			except Exception as e:
				print("load_quote_date failed ... "+quote['Symbol']+"/"+quote['Name']+"\n")
				if (not is_retry):
					time.sleep(2)
					self.load_quote_data(quote,start_date,end_date,True,counter)
		return quote

	def get_columns(self,quote):
		columns=[]
		if(quote is not None):
			for key in quote.keys():
				if(key=='Data'):
					for data_key in quote['Data'][-1]:
						columns.append("data."+data_key)
				else:
					columns.append(key)
			columns.sort()
		return columns


	def data_export(self,all_quotes,export_type_array,file_name):
		start=timeit.default_timer()
		directory=self.export_folder
		if(file_name is None):
			file_name=self.export_file_name
		if not os.path.exists(directory):
			os.makedirs(directory)
		if(all_quotes is None or len(all_quotes)==0):
			print("no data to export ..."+"\n")
		if('json' in export_type_array):
			print("start export to JSON file ... \n")
			f=io.open(directory+"/"+file_name+'.json','w',encoding=self.charset)
			json.dump(all_quotes,f,ensure_ascii=False)
		if('csv' in export_type_array):
			print("start export to CSV file ...\n")
			columns=[]
			if(all_quotes is not None and len(all_quotes)>0):
				columns=self.get_columns(all_quotes[0])
			writer=csv.writer(open(directory+"/"+file_name+'.csv','w',encoding=self.charset))
			writer.writerow(columns)

			for quote in all_quotes:
				if('Data' in quote):
					for quote_data in quote['Data']:
						try:
							line=[]
							for column in columns:
								if(column,find('data.')>-1):
									if(column[5:] in quote_data):
										line.append(quote_data[column[5:]])
								else:
									line.append(quote[column])
							writer.writerow(line)
						except Exception as e:
							print(e)
							print("write csv error "+quote)
		print("export is complete... time cost "+str(round(timeit.default_timer()-start))+"s"+"\n")




	def run(self):
		output_types=[]
		if(self.output_type=="json"):
			output_types.append("json")
		elif(self.output_type=="csv"):
			output_types.append("csv")
		elif(self.output_type=="all"):
			output_types=['json','csv']

		if(self.reload_data=='Y'):
			self.data_load(self.start_date,self.end_date,output_types)


if __name__=='__main__':
	args = option.parser.parse_args()
	stockh = Stockholm(args)
	stockh.run()
	print("A")








