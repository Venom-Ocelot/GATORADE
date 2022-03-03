def process_data(data):
	new_l = data.split('\n\n')
	dct = {}
	for h in new_l:
		tp = ''
		for y in h.split('\n')[1::]:
			tp+=y+'\n'
		tp = tp[:-1]
		dct[h.split('\n')[0]] = tp
	return(dct)

data = process_data(open('file.txt','r').read())
print(data)
new_fl = open('file.txt','w')
lk = list(data.keys())
lk = list(set(lk))
print('>>>Writing new data...')
for g in lk:
	if len(g)>0:
		if g == lk[-1]:
			new_fl.write(g+'\n'+data[g])
		else:
			new_fl.write(g+'\n'+data[g]+'\n\n')

new_fl.close()