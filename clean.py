import pandas as pd
import numpy as np

def clean():
	df = pd.read_csv('index.txt', sep="\t", index_col='pid', names=['folder', 'pdfid', 'pid', 'title'])
	
	#read in papers to df and drop unnecessary columns
	papers = pd.read_csv('Papers.txt', sep="\t", names=['pid', 'title_case', 'title', 'year', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'cid', 'drop2'])
	for col in ['title', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'drop2']:
		del papers[col]

	#read in paper keywords to df
	keywords = pd.read_csv('PaperKeywords.txt', sep="\t", names=['pid', 'keyword', 'kid']_
	del papers['kid']
	
	#read in paper author affiliations to df
	affiliation = pd.read_csv('PaperAuthorAffiliation.txt', sep="\t", names=['pid', 'aid', 'fid', 'aff_org', 'aff', 'sid'])
	del affiliation['aff_org']

	#read in authors to df
	authors = pd.read_csv('Authors.txt', sep="\t", names=['aid', 'aut'])

	print("FIRST ONE")
	print(df.head())
	print("SECOND ONE")
	print(papers.head())
	df = df.join(papers)
	df = df.join(keywords)
	df = df.join(affiliation)
	df = pd.merge(df, authors, on='aid')	

	print(df.head())

clean()
