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

####### this currently does not work as expected!


#print("Number of unlinked terms found: " + ((string.count(term) - string.count(linked_term))).__str__())
#print("Number of linked terms found: " + str(string.count(linked_term)))



for word in string_split:
    print("now on this word...")
    print(word)
    #for linked_term in linked_links:
    #    print("Now cross referencing with the following linked_term")
    #    print(linked_term)
    ### FOR NOW, there's no real good reason to check for punctuation IF the word is a
    #### already linked term even with punctuation! The main goal of this script/function
    #### is to search for NAKED TERMS that SHOULD be linked and LINK THEM!
    #### You can use a different function/script for now for checking for
    #### for NOVEL links that are not in the linked list
    if word in linked_links:
        print("found a match for a linked term!")
        print(word)
        new_string = new_string + " " + word
        print(new_string)
        continue
    #for term in naked_links:
    #    print("Now checking the following NAKED LINK")
    #    print(term)
    if word in naked_links:
        print("found a match for an UNLINKED term")
        print(word)
        new_link = "[[" + word + "]]"
        new_string = new_string + " " + new_link
    else:
        # let's give this word one last chance in case it:
        ### 1. is actually a LINKED term with punctuation
        ### 2. is a irrelevant word with punctuation
        ### 3. is a NAKED link with punctuation!!!!!
        print("Giving this word one last chance...")
        if re.search(r"[.,\s]+(?!\w+])", word):
            print("found punctuation!")
            word_punct = re.findall( r'\w+|[^\s\w]+', word)
            print(word_punct)
            ## SINCE we did not check for LINKED TERMS WITH PUNCTUATION we will do that here, if we find that there is bracket found.. just BREAK LOOP and move on...
            ## BUT IF first item of list is NOT a bracket and is infact the term, THEN proceed with re-checking to see if that NON-LINKED, BUT PUNCTUATED WORD
            ### is infact a NAKED LINK!!!!
            if word_punct[0] == term:
                word_punct[0] = linked_term
                #word_punct.remove(term)
                #word_punct.replace(linked_term)
                print("linked this term!")
                print(word_punct)
                final_term = ''.join(word_punct)
                print(final_term)
                new_string = new_string + " " + final_term

        else:
            print("no punctuation found")
            final_term = word.replace(term, linked_term)
            print(final_term)
            new_string = new_string + final_term
            continue
    #new_string = new_string + " " + word
    #print("done with this word! here is your string so far")
    #print(new_string)
print("all done! here is your processed string")
print(new_string)

## save new_string to MD file


#### when dealing with punctuation, you have to check for punctuation first 
# and strip it first before checking the word or else punctuated terms will always fail

