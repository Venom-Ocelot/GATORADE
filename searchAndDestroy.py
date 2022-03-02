import os

# filesystem
spath = os.getcwd()
directories = os.listdir()

# search and destroy
def process_data(data):
    # This function alone is able to create a dictionary and make
    print("A new variable named datasplit is declared. The parameter it takes is named data.\n")
    print(".split(\\n\\n) is being called upon the data that is inputted and assigned to the variable datasplit.")
    print("This function takes the entire set of data and separates it into an array by double newlines.\n")
    datasplit = data.split('\n\n')
    print("The array datasplit is:")
    print(f"{datasplit}\n")

    print("A new dictionary is being created named dct.")
    dct = {}
    print("New for loop created. For every enhancer in the variable datasplit, this is being done: ")
    for enhancer in datasplit:
        currentenhancer = enhancer.split('\n\n')
        print(f"\t-Current enhancer: {currentenhancer}\n")
        new_data = ''
        print("\t-The variable new_data has been set to ''\n")
        print("\t-The variable chunk is created and is set to enhancer.split('\\n')[1:], which selects")
        print("\t-the second item in the array, aka the DNA sequence under the enhancer, and selects every line after that")
        print("\t-until the end of the list.\n")
        chunk = enhancer.split('\n')[1:]
        print("\t-Printing chunk:")
        print(f'\t{chunk}\n')

        print("New for loop within datasplit for loop")
        print(f"For every item in the chunk array, if the for loop counter is not equal to the length of chunk({len(chunk)}) minus one,")
        print("we add line to the variable new_data plus a newline and add 1 to the counter. Otherwise, we just add p")
        print("to the new_data variable.\n")
        cn = 0
        for line in chunk:
            # print(p)
            if cn != len(chunk) - 1:
                print("If statement has passed.")
                # print(f"Adding {line} + \\n to new_data")
                new_data += line + '\n'
                # print(new_data)
                cn += 1
            else:
                print("Else statement has been passed.")
                # print(f"Adding {line} to new_data.")
                new_data += line
                # print(new_data)
                print("Assigning the enhancer name to the dictionary definition, new_data.\n")
                dct[enhancer.split('\n')[0].strip()] = new_data
                print("\nThe enhancer name added is:")
                print(enhancer.split('\n')[0].strip())
                print("\nThe sequence assigned to it is:")
                print(new_data)
                print('\n')

    return dct

print(directories)
# for directory in directories:
# 	print(directory)

for directory in directories:
    print('>>>Reading and processing the files...')

    print(directory)
    if "main.py" != directory and "enhancersAdded.fasta" != directory:
        data_1 = process_data(open(f'{spath}/{directory}/neg.fasta', 'r').read())
        data_2 = process_data(open(f"{spath}/{directory}/crms.fasta", 'r').read())

        temp_data_1 = []
        for key in data_1:
            if key in data_2:
                temp_data_1.append(key)

        print(f'>>>Overlapping data found : {temp_data_1}')
        new_fl = open(f'{spath}/{directory}/neg.fasta', 'w')
        lk = list(data_1.keys())
        print('>>>Writing new data...')
        for g in data_1:
            if g not in temp_data_1:
                if g == lk[-1]:
                    new_fl.write(g + '\n' + data_1[g])
                else:
                    new_fl.write(g + '\n' + data_1[g] + '\n\n')
    new_fl.close()
    print(
        'File has been processed any overlapping data is removed from first file. \nAll Processed done, Please Close the window')

