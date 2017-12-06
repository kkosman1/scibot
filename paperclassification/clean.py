import pandas as pd
import numpy as np

def clean():
	file_name = 'unique_counts.txt'
	df = pd.read_csv('index.txt', dtype=str, sep="\t", index_col='pid', names=['folder', 'pdfid', 'pid', 'title'])
	
	#read in papers to df and drop unnecessary columns
	papers = pd.read_csv('Papers.txt', sep="\t", dtype=str, names=['pid', 'title_case', 'title', 'year', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'cid', 'drop2'])
	for col in ['title', 'date_of_proceeding', 'doi', 'conf_full_name', 'drop1', 'drop2']:
		del papers[col]

	#read in paper keywords to df
	keywords = pd.read_csv('PaperKeywords.txt', sep="\t", dtype=str, names=['pid', 'keyword', 'kid'], index_col='pid')
	del keywords['kid']	

	#read in paper author affiliations to df
	affiliation = pd.read_csv('PaperAuthorAffiliations.txt', sep="\t", dtype=str, names=['pid', 'aid', 'fid', 'aff_org', 'aff', 'sid'], index_col='pid')
	del affiliation['aff_org']

	#read in authors to df
	authors = pd.read_csv('Authors.txt', sep="\t", dtype=str, names=['aid', 'aut'])

	#join the papers together
	df = papers.join(df)
	df = df.join(keywords)
	df = df.join(affiliation)
	df = pd.merge(df, authors, how='left')	
	df = df.drop_duplicates(subset='pid')

	#print to file
	df.to_csv('database.txt', sep='\t')

	#print out the unique counts
	df2 = df.apply(pd.Series.nunique)
	df2.to_csv(file_name, sep='\t')

clean()
