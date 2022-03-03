import os
import shutil

# filesystem
spath = os.getcwd()
directories = os.listdir()

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


print("Directories:")
print(directories)
# Get size of path
sizeOfPath = len(os.listdir(spath))
print(f"Sets found: {sizeOfPath}\n")

print("Assigning the sets to a path...")
# Iterates over the directory names and proceeds to look for the path with the training set name named crms.fasta,
# reads the file, and copies the contents to new_fl, aka a file that will be placed above the training set directories.
# This file contains all of the crms from every directory.
print("Beginning a for loop that will iterate over all of the training set names such as adult midgut, or antenna.")
print("Starting...\n")
for directory in directories:
    if directory != __file__:
        print('crms path:')
        data_1 = process_data(open(spath+'/'+directory+'/'+'crms.fasta', 'r').read())
        print(data_1)

        # creation of file
        new_fl = open(f'{spath}/neg.fasta', 'a')
        lk = list(data_1.keys())
        print("printing lk[-1]")
        print(lk[-1])
        for g in data_1:
            if g == lk[-1]:
                print("\nThe values match. Writing (g + newline + data_1[g]) to new_fl\n")
                print("For reference, will print out each part of it.")
                print("Printing")
                print(g)
                print('\n')
                print(data_1[g])
                new_fl.write(g + '\n' + data_1[g]+'\n')
            else:
                print(f"Since lk({lk[-1]}) is not equal to g({g}), we are going to write g + newline + data_1[g] + newlinenewline")
                new_fl.write(g + '\n' + data_1[g] + '\n\n')
        new_fl.close()

# We copy the file we created and paste it into each directory as neg.fasta
for directory in directories:
    if directory != "main.py" and directory != "neg.fasta":
        shutil.copy(f"{spath}/neg.fasta", f"{spath}/{directory}/")

# Finally, we print it out again as a sort of "receipt." It is named "enhancersAdded.fasta"
os.rename(f'{spath}/neg.fasta', 'enhancersAdded.fasta')


# search and destroy

# searchAndDestroy.py finds matches between a crms and a neg file within a training set and removes any matches from the
# neg file.

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

