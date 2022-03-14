import os

new_lst = open ("newlst.lst", "w")

for x in os.listdir():
    if x != "newlst.lst":
        new_lst.write(f"{os.getcwd()}/{x}\n")
new_lst.close()

print("A new .lst file has been created for use with SCRMSHAW.")
