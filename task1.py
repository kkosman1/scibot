def task_1(files):
	paper_info = {}
	authors = {}
	for f in files:
		fd = open(f)
		if f=="Authors.txt":
			for line in fd:
				aid, author = line.split("\t")
				authors[aid]={}
				authors[aid]['name']=author
				authors[aid]['pcount']=0
				authors[aid]['titles']=[]
		if f=="PaperAuthorAffiliations.txt":
			for line in fd:
				pid, aid, fid, aff_org, aff, sid = line.split("\t")
				if pid not in paper_info:
					paper_info[pid]={}
				paper_info[pid]['aid']=aid
				paper_info[pid]['fid']=fid
				paper_info[pid]['aff']=aff
				if aid in authors.keys():
					paper_info[pid]['author']=authors[aid]['name']
					authors[aid]['pcount']+=1
		if f=="Papers.txt":
			for line in fd:
				info = line.split("\t")
				pid = info[0]
				if pid not in paper_info:
					paper_info[pid]={}
				paper_info[pid]['title_case'] = info[1]
				paper_info[pid]['title'] = info[2]
				paper_info[pid]['year'] = info[3]
#				if paper_info[pid]['aid'] in authors.keys():
#					authors[paper_info[pid]['aid']]['titles'].append(len(info[2]))
		if f=="PaperKeywords.txt":
			for line in fd:
				pid, keyword, kid = line.split("\t")
				if pid not in paper_info:
					paper_info[pid]={}
				paper_info[pid]['keyword']=keyword

	return (paper_info, authors)

papers, authors = task_1(["Authors.txt", "PaperAuthorAffiliations.txt", "Papers.txt", "PaperKeywords.txt"])

print "Papers: " + str(len(papers))
print "Authors: " + str(len(authors))

#author_avgs={}
#for aid in authors.keys():
#	if authors[aid]['pcount']>3:
#		author_avgs[authors[aid]['name']] = sum(authors[aid]['titles'])/len(authors[aid]['titles'])

#for i in range(3):
#	max_value = max(author_avgs.values())
#	max_key = [k for k, v in author_avgs.items() if v==max_value]
#	print max_key
#	del author_avgs[max_key]

for pid in papers.keys():
	if authors[papers[pid]['aid']]['pcount'] > 3:
		words = papers[pid]['keyword'].split(" ")
		if "matrix" in words:
			print papers[pid]['author']

