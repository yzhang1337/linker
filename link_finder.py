## Scripts needed
## script to read in the text and find and replace terms for the bracketted terms
#### link_finder.py
## script to read in all MD files and aggregate all the bracketted terms
#### link_aggregator.py
##### found links are written to links.txt (serves as running list of links to date)
###### this script will then also search for filenames from that list and makes new files with the new terms 
import re
import os


## dir where notes are located
notes = os.listdir('/Users/yz/links/notes')

## links.txt represents the running list of terms to be converted to bracketted wikilinks
### the below code reads in already existing links within links.txt
### and links any new unlinked terms! 
with open("/Users/yz/links/links.txt") as f:
    links = f.readlines()
    links = [x.strip() for x in links]
    for term in links:
        link_term = "[[" + term + "]]"
        for note in notes:
            note_text = open('/Users/yz/links/notes/' + note).read()  
            if term in note_text:
                print(term)
                with open('/Users/yz/links/notes/' + note, 'w') as f:
                    f.write(note_text.replace(term, link_term))
                    print("replaced " + term + " with " + link_term + " in " + note)
            else:
                print("no match for " + term + " in " + note)

print("all done!")

## have to fix the issue that the extra brackets are getting added to already bracketed terms!

### if the term is already bracketed, then don't do anything!
#### if term in note_text:
##### check if term -1 and term +1 are brackets, if so, skip!
#### if the term is not already bracketed, then add the brackets!

       