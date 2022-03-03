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

    return (dct)

print("\nGrabbing directories within the training sets folder..\nDirectories found:")
print(directories)
sizeOfPath = len(os.listdir())
print(f"The number of directories detected within {spath} is: {sizeOfPath}\n")

print("Assigning the sets to a path...")
# Iterates over the directory names and proceeds to look for the path with the training set name named crms.fasta,
# reads the file, and copies the contents to new_fl, aka a file that will be placed above the training set directories.
# This file contains all of the crms from every directory.
print("Generating a neg.fasta file...")
for directory in directories:
    if directory != "enhancersAdded.fasta":
        # crms general path
        data_1 = process_data(open(f'{spath}/{directory}/crms.fasta', 'r').read())
        print(f"crms.fasta found! Using {directory}/crms.fasta")
        print("Data from crms file processed.\n")

        new_fl = open('neg.fasta', 'a')
        # the .keys() function is able to grab the first dictionary word, if dict = a:b, .keys() returns 'a'
        lk = list(data_1.keys())
        print(lk[-1])
        for g in data_1:
            # lk [-1] is grabbing the very last enhancer sequence name in the dictionary.
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

for directory in directories:
    shutil.copy("neg.fasta", f"{spath}/{directory}/")

print("Renaming the neg.fasta file contained in the same directory as the training sets to 'enhancersAdded.fasta'")
os.rename('neg.fasta', 'enhancersAdded.fasta')
