# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                #append the individual words to the list and convert letters
                #to lowercase for case sensitivity
                lower_case = w.lower()
                keys.add(lower_case)
                #check if word is alread in hashmap
                if ht.contains_key(lower_case):
                    #increase word count and insert into hasmap and update count
                    val = (ht.get(lower_case) + 1)
                    ht.put(lower_case, val)
                else:
                    #insert into hasmap with initial count being one 1 if not in hashmap already
                    ht.put(lower_case, 1)
    #create a new list if words
    word_list = []
    #loop thru the list
    for k in keys:
        index = ht._hash_function(k) % ht.capacity
        temp = ht._buckets[index]
        #add tuples to list containing word and count
        linked_node = temp.contains(k)
        word_list.append((linked_node.key, linked_node.value))
    #sort list in descending order
    word_list.sort(key = lambda tup: tup[1], reverse = True)
    #return list of top words
    return word_list[0:number]


# print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE