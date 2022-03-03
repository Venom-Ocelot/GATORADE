# GATORADE

This is the GATORADE repository created for Halfon Labs. 

Files:
- gatorade.py V.1.2
- add-only.py V.1.1
- searchAndDestroy.py 

HELP:

(1) gatorade.py
gatorade.py should be placed within the directory containing the training sets.
The script will iterate through every training set and create a neg.fasta file of all the crm's detected. It will then add this file to every training set so that each training set contains a neg.fasta file, and a crms.fasta file. gatorade.py will then run an integrated version of searchAndDestroy.py, which will detect matches within the crms.fasta files and the neg.fasta files, and delete any matches from the set-specific neg.fasta file.

(2)
add-only.py should be placed within the directory containing the training sets.
This script will find all of the crms.fasta files within a sets folder and append them all to a negs.fasta file. (WARNING: This will not check for duplicates within the negs.fasta file. See Upcoming Changes for more information.)

(3)
searchAndDestroy.py
This script will search for all crms.fasta and neg.fasta files within a training set's directory, removing all duplicates found between neg.fasta and crms.fasta  from neg.fasta 

# UPCOMING CHANGES
- gatorade.py V.1.3 will scan the dictionary for duplicates before appending to the negs file. 
- add-only.py V.1.1 will reflect this change.


