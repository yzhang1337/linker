import re
import os


### Read in already known links from a text file
#term = "link"
#linked_term = "[[link]]"
l = open("links.txt", "r")
naked_links = l.readlines()
naked_links = [x.strip() for x in naked_links]
print("here are the links that will be searched")
print(naked_links)

linked_terms = []
for term in naked_links:
    linked_term = "[[" + term + "]]"
    linked_terms.append(linked_term)
print("here are the linked variants")
print(linked_terms)