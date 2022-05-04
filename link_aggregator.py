import re
import os
## now lets see if we can return all the bracketted terms into a list
print("Here are your bracket terms")
all_terms = re.findall(r"\[([A-Za-z0-9_]+)\]", string)
print(all_terms)

## lets write this to a text file

for term in all_terms:
    print(term)
    with open("links.txt", "a") as f:
        f.write(term + "\n")
print("all done!")
