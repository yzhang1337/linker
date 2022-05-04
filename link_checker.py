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

linked_links = []
for term in naked_links:
    linked_term = "[[" + term + "]]"
    linked_links.append(linked_term)
print("here are the linked variants")
print(linked_links)


## new string to build on
new_string = ""

#print(string.count(term))
#print(string.count(linked_term))
f = open("test_string.md", "r")
string = f.read()
print("Here is the input string...")
print(string)

## split method
string_split = string.split()
print("Here is the input string after it has been SPLIT!")
print(string_split)
print('\n')

### naked_links represents the list of all links; linked_links represents the list of already discovered links
#### term = a single item within the list of naked_links
#### linked_term = a single item within the list of linked_links
### Let's loop thru the naked_links list and see how many any of each term are in the string
### Then let's loop thru the linked_links list and see how many existing links of are already in the string
### This is done PER item in each list and counts are printed accordingly

for linked_term in linked_links:
    print(linked_term)
    print(string.count(linked_term))
    print('\n')    
    for term in naked_links:
        print(term)
        print(((string.count(term) - string.count(linked_term))).__str__())
        print('\n')

#print("Number of unlinked terms found: " + ((string.count(term) - string.count(linked_term))).__str__())
#print("Number of linked terms found: " + str(string.count(linked_term)))



for word in string_split:
    print("now on this word...")
    print(word)
    if re.search(linked_term, word):
        print("found a match for a linked term!")
        print(word)
        if re.search(r"[.,\s]+(?!\w+])", word):
            print("found punctuation!")
            print(word)
            word_punct = re.findall("[.,\s]+(?!\w+])", word)
            print(word_punct)
            new_string = new_string + " " + linked_term + word_punct[0]
        else:
            print("no punctuation found")
            new_string = new_string + word
        continue
    if re.search(term, word):
        print("found a match for an UNLINKED term")
        print(word)
        if re.search(r"[.,\s]+(?!\w+])", word):
            print("found punctuation!")
            word_punct = re.findall( r'\w+|[^\s\w]+', word)
            print(word_punct)
            if word_punct[0] == term:
                word_punct[0] = linked_term
                #word_punct.remove(term)
                #word_punct.replace(linked_term)
                print("linked this term!")
                print(word_punct)
                final_term = ''.join(word_punct)
                print(final_term)
                new_string = new_string + " " + final_term
                continue
        else:
            print("no punctuation found")
            final_term = word.replace(term, linked_term)
            print(final_term)
            new_string = new_string + final_term
    new_string = new_string + " " + word
    print("done with this word! here is your string so far")
    print(new_string)
print("all done! here is your processed string")
print(new_string)

## save new_string to MD file

