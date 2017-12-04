import pandas as pd
import numpy as np

def clean():
	df = pd.read_csv('index.txt', sep="\t", index_col='pid', names=['folder', 'pdfid', 'pid', 'title'])
	#df['title'].str.lower()
	
	#read in papers to df and drop unnecessary columns
	papers = pd.read_csv('Papers.txt', sep="\t", names=['pid', 'title_case', 'title', 'year', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'cid', 'drop2'])
	for col in ['title', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'drop2']:
		del papers[col]
	#papers['title'].str.lower()
	
	print("FIRST ONE")
	print(df.head())
	print("SECOND ONE")
	print(papers.head())
	newdf = df.join(papers)
	
	print(newdf.head())

clean()
