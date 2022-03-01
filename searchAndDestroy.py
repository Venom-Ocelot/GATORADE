def process_data(data):
	new_l = data.split('\n\n')
	dct = {}
	for h in new_l:
		new_data = ''
		nd = h.split('\n')[1::]
		cn=0
		for p in nd:
			if cn!=len(nd)-1:
				new_data+=p+'\n'
				cn+=1
			else:
				new_data+=p
		dct[h.split('\n')[0].strip()] = new_data

	return(dct)

import os

spath = f"{os.getcwd()}"

directories = os.listdir(spath)
print(directories)
# for directory in directories:
# 	print(directory)

for directory in directories:
	print('>>>Reading and processing the files...')

	print(directory)
	if "searchAndDestroy.py" != directory:
		data_1 = process_data(open(f'{directory}/neg.fasta', 'r').read())
		data_2 = process_data(open(f"{directory}/crms.fasta",'r').read())

		temp_data_1 = []
		for key in data_1:
			if key in data_2:
				temp_data_1.append(key)

		print(f'>>>Overlapping data found : {temp_data_1}')
		new_fl = open(f'{directory}/neg.fasta','w')
		lk = list(data_1.keys())
		print('>>>Writing new data...')
		for g in data_1:
			if g not in temp_data_1:
				if g == lk[-1]:
					new_fl.write(g+'\n'+data_1[g])
				else:
					new_fl.write(g+'\n'+data_1[g]+'\n\n')
	new_fl.close()
	print('File has been processed any overlapping data is removed from first file. \nAll Processed done, Please Close the window')
