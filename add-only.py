import os
import shutil


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

spath = f"{os.getcwd()}/new74Tsets_Feb2020_oldCombined114"
print(spath)

print("\nGrabbing directories within the training sets folder..")
directories = os.listdir(spath)
print("Directories found:")
print(f'{directories}')
# Get size of path
sizeOfPath = len(os.listdir(spath))
print(f"The size of the path is {sizeOfPath}\n")
print("Assigning the directories to a path...")

print("Beginning a for loop that will iterate over all of the training set names such as adult midgut, or antenna.")
print("Starting...\n")
for directory in directories:
    if directory != "enhancersAdded.fasta":
        print('crms path:')
        data_1 = process_data(open(spath+'/'+directory+'/'+'crms.fasta', 'r').read())
        print(data_1)


        print("Now that all of the data has been processed, we need to print it all out to a text document.")
        new_fl = open(f'neg.fasta', 'a')
        print("\nCreating a new variable called lk, and there is a new function that is being applied I'm not sure about...")
        lk = list(data_1.keys())
        print("printing lk")
        print(lk)
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

for directory in directories:
    shutil.copy(f"neg.fasta", f"new74Tsets_Feb2020_oldCombined114/{directory}/")

os.rename('neg.fasta', 'enhancersAdded.fasta')

# # search and destroy
# for directory in directories:
#     print('crms path:')
#     y = f"/home/gator/PycharmProjects/HalfonLabs/new74Tsets_Feb2020_oldCombined114/{directory}/crms.fasta"
#     print(y)
#     z = f"/home/gator/PycharmProjects/HalfonLabs/new74Tsets_Feb2020_oldCombined114/{directory}/neg.fasta"
#     print("negs path:")
#     print(z)
#     print('>>>Reading and processing the files...')
#
#     data_1 = process_data(open(y, 'r').read())
#     data_2 = process_data(open(z, 'r').read())
#
#     temp_data_1 = []
#
#     print("temp_data_1 is created as an array.")
#
#     print("for every item in data_1:")
#     print("if the item is located in data_2")
#     print("the item is added to temp_data_1")
#     print("\nMy guess is that this item is the name of the enhancer sequence. If it is, verify and rename.")
#
#     for key in data_1:
#         print(f"Key: {key}")
#         if key in data_2:
#             print(f'\n{key} was found in data_1 and now data_2. appending {key} to temp_data_1')
#             temp_data_1.append(key)
#
#     print(f'>>>Overlapping data found : {temp_data_1}')
#     print("Creating a new variable named new_fl, opening the negs file for each directory.")
#     print(f"The directory currently being worked on is new74Tsets_Feb2020_oldCombined114/{directory}/neg.fasta")
#     new_fl = open(f'new74Tsets_Feb2020_oldCombined114/{directory}/neg.fasta', 'w')
#     print("\nCreating a new variable called lk, and there is a new function that is being applied I'm not sure about...")
#     lk = list(data_1.keys())
#     print('>>>Writing new data...')
#
#     print("New for loop created, iterating over items g in the variable data_1\n")
#     for g in data_1:
#         print("Checking if item g is not in temp_data_1")
#         if g not in temp_data_1:
#             print(f"\nItem g ({g}) is not in temp_data_1.\nChecking to see if item g ({g}) is equal to the variable lk[-1]")
#             print(f"For reference, lk[-1] is {lk[-1]}.")
#             if g == lk[-1]:
#                 print("\nThe values match. Writing (g + newline + data_1[g]) to new_fl\n")
#                 print("For reference, will print out each part of it.")
#                 print("Printing")
#                 print(g)
#                 print('\n')
#                 print(data_1[g])
#                 new_fl.write(g + '\n' + data_1[g])
#             else:
#                 print(f"Since lk({lk[-1]}) is not equal to g({g}), we are going to write g + newline + data_1[g] + newlinenewline")
#                 new_fl.write(g + '\n' + data_1[g] + '\n\n')
#                 print(f"NEW DATA WRITTEN: {data_1[g]}")
#     new_fl.close()
#
#
#
#
