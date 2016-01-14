import collections
"""
Jonathan McAlexander 
Katherine Bielawiec

This is a practice program designed to test our basic understanding
of the Python language and usage of lists and dictionaries.
"""
############################################################
# Problem 1a

def compute_max_word_length(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    return max(text.split())
    # END_YOUR_CODE

############################################################
# Problem 1b

def manhattan_distance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    return (abs(loc2[1]-loc1[1])) + (abs(loc2[0]-loc1[0]))
    # END_YOUR_CODE

############################################################
# Problem 1c

def sparse_vector_dot_product(vec1, vec2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as Counters, return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    list_of_keys = (vec1+vec2).keys()  # obtain all the possible dimensions for the vectors
    dot_products = []
    for thing in list_of_keys: 
        dot_products.append(vec1[thing]* vec2[thing]) 
   
    return sum(dot_products)
   
    # END_YOUR_CODE

############################################################
# Problem 1d

def compute_most_frequent_word(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair: 
    the set of words that occur the maximum number of times, and
	their count, i.e. (set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.Counter().
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    countable_set = collections.Counter(text.split())     # Counter with words and their occurrences
    ordered_count = countable_set.most_common()       # sorted tuples of countable
    max_count = ordered_count[0][1]
    max_set = [i_tuple[0] for i_tuple in ordered_count if i_tuple[1] == max_count]   
    return (set(max_set), max_count)
    # END_YOUR_CODE

############################################################
# Problem 1e

def correct_parentheses(expression):
    """
    Checks if a given expression has a correct combination of opening and
    closing parentheses. (a+b)*c returns True, ((a+b) returns False.
    Hint: use stack
    """
    # BEGIN_YOUR_CODE 
    expression_list_as_characters = list(expression)
    parenthesis_count = collections.Counter(expression_list_as_characters)
    if parenthesis_count["("] == parenthesis_count[")"]:
        return True
    else:
        return False
    # END_YOUR_CODE
    
############################################################
# Problem 1f

def nested_parentheses(expression):
    """
    Must be done recursively. 
    Given a string, return true if it is a nesting of zero or more pairs of parenthesis, 
    like "(())" or "((()))". Suggestion: check the first and last chars, 
    and then recur on what's inside them. 

    nestedParentheses("(())")  true
    nestedParentheses("((()))")  true
    nestedParentheses("(((x))")  false
    
    Use this link to practice in Java first:
    http://codingbat.com/prob/p183174
    """
    # BEGIN_YOUR_CODE 

    if expression is "":
        return True
    elif expression[0] is '(' and expression[-1] is ')':
        return nested_parentheses(expression[1:-1])
    else:
        return False
    
    # END_YOUR_CODE   
 