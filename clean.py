import pandas as pd
import numpy as np

def clean():
	df = pd.read_csv('index.txt', sep="\t", index_col='pid', names=['folder', 'pdfid', 'pid', 'title'])
	print(df)
