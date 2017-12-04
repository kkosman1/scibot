import pandas as pd
import numpy as np

def clean():
	df = pd.read_csv('index.txt', sep="\t", index_col='pid', names=['folder', 'pdfid', 'pid', 'title'])
	df['pid'] = df['pid'].astype(str)
	
	#read in papers to df and drop unnecessary columns
	papers = pd.read_csv('Papers.txt', sep="\t", names=['pid', 'title_case', 'title', 'year', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'cid', 'drop2'])
	for col in ['title', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'drop2']:
		del papers[col]
	papers['pid'] = papers['pid'].astype(str)

	#read in paper keywords to df
	keywords = pd.read_csv('PaperKeywords.txt', sep="\t", names=['pid', 'keyword', 'kid'])
	del keywords['kid']
	keywords['pid'] = keywords['pid'].astype(str)	

	#read in paper author affiliations to df
	affiliation = pd.read_csv('PaperAuthorAffiliations.txt', sep="\t", names=['pid', 'aid', 'fid', 'aff_org', 'aff', 'sid'])
	del affiliation['aff_org']
	affiliation['pid'] = affiliation['pid'].astype(str)
	affiliation['aid'] = affiliation['aid'].astype(str)

	#read in authors to df
	authors = pd.read_csv('Authors.txt', sep="\t", names=['aid', 'aut'])
	authors['aid'] = authors['aid'].astype(str)

	print("FIRST ONE")
	print(df.head())
	print("SECOND ONE")
	print(papers.head())
	df = df.join(papers)
	df = pd.merge(df, keywords, on='pid')
	df = pd.merge(df, affiliation, on='pid')
	#df = df.join(keywords)
	#df = df.join(affiliation)
	df = pd.merge(df, authors, on='aid')	

	print(df.head())

clean()
