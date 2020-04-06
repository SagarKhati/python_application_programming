import re

pattern = 'for'
text = 'information'
if re.search(pattern, text):
    print('Yes')


########################################################
    
    
####### Regex Functions #########
''' 
Function	Description
 match	     This method matches the regex pattern in the string with the optional flag. It returns true if a match is found in the string otherwise it returns false.
 search	     This method returns the match object if there is a match found in the string.
 findall	 It returns a list that contains all the matches of a pattern in the string.
 split	     Returns a list in which the string has been split in each match.
 sub	     Replace one or many matches in the string.
'''

######## Meta-Characters ########  
'''
Metacharacter    Description	                                                       Example
    []	          It represents the set of characters.	                               "[a-z]"
    \	          It represents the special sequence.	                               "\r"
    .	          It signals that any character is present at some specific place.	   "Ja.v."
    ^	          It represents the pattern present at the beginning of the string.	   "^Java"
    $	          It represents the pattern present at the end of the string.	       "point"
    *	          It represents zero or more occurrences of a pattern in the string.	   "hello*"
    +	          It represents one or more occurrences of a pattern in the string.	   "hello+"
    {}	          The specified number of occurrences of a pattern the string.	       "java{2}"
    |	          It represents either this or that character is present.	           "java|point"
    ()	          Capture and group
'''

######## Special Sequences ########
'''
Character	Description
 \A	         It returns a match if the specified characters are present at the beginning of the string.
 \b	         It returns a match if the specified characters are present at the beginning or the end of the string.
 \B	         It returns a match if the specified characters are present at the beginning of the string but not at the end. 
 \d	         It returns a match if the string contains digits [0-9].
 \D	         It returns a match if the string doesn't contain the digits [0-9].
 \s	         It returns a match if the string contains any white space character.
 \S	         It returns a match if the string doesn't contain any white space character.
 \w	         It returns a match if the string contains any word characters.
 \W	         It returns a match if the string doesn't contain any word.
 \Z	         Returns a match if the specified characters are at the end of the string.
'''

######## Sets ########
'''
Set	         Description
 [arn] 	      Returns a match if the string contains any of the specified characters in the set.
 [a-n]	      Returns a match if the string contains any of the characters between a to n.
 [^arn]	      Returns a match if the string contains the characters except a, r, and n.
 [0123]	      Returns a match if the string contains any of the specified digits.
 [0-9]	      Returns a match if the string contains any digit between 0 and 9.
 [0-5][0-9]   Returns a match if the string contains any digit between 00 and 59.
 [a-zA-Z]	  Returns a match if the string contains any alphabet (lower-case or upper-case).
'''



#######################################################################################################################

  
str = "How are you. How is everything"  
matches = re.findall("How", str)  
print(matches)  
print(matches)  


str = "How are you. How is everything"  
matches = re.search("How", str)  
print(type(matches))  
print(matches) #matches is the search object  


str = "How are you. How is everything"  
matches = re.search("How", str)  
print(matches.span())  
print(matches.group())  
print(matches.string) 