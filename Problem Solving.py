#!/usr/bin/env python
# coding: utf-8

# In[1]:


True/False :

- Comparison ==,!=,<,>
- identity is is not
- Membership in not in 
- Logical Operators and or not 

== => values
is => memory location

False values : None "" 0 [] () {}

enumerate for index,value in enumerate(iterable):

Keys, values => items()

for else:

[start:end:stride] 2 => every seco char -1 => 1 => left to right

s[100] => IndexError

Lists: add : append extend insert Update: l[index] = new_value

Delete:
    pop => index
    remove => value
    clear => empty list 
    del => del ref 

l1 + l2 =>
l1 * 2

Dict : Add: d[key] = value setdefault(key,default_value) => return the existing value

Update:
    d[key] = new_value

delete:
    pop("key")
    popitem() 
    clear
    del

mutable
unordered
all the keys should be unique
all the keys should be immutable => int,str,float,tuple
Sets:

- mutable
- unordered 
- all the elemnts should be unique 
- all the elemnts should be immutable 

Iterable : list tuple str dict set Not iterable : int float

print(dir(list ))

help(list)

1.find the missing number in given integer array of 1 to 10. l = [1,2,3,4,5,6,7,7,9,10]

=> Range(1,11)

=> Sum of n natural nos : n (n+1) / 2 sum => 1 to 10 sum_list
missing element = sum - sum_list

=> Sets only unique elemnts


# In[3]:


input_nums = [1,2,3,4,5,6,7,9,10]
n = 10 
expected_sum = n * (n + 1) / 2
actual_sum = sum(input_nums)
missing_element =  expected_sum - actual_sum
print(missing_element)


# input_nums = [1,2,3,4,5,6,7,9,10]
# all_nums = list(range(1,11))
# missing_elements = []
# 
# for value in all_nums:
#     if value not in input_nums:        
#         missing_elements.append(value)
# print(missing_elements)

# In[ ]:


# 2.Find an element in array such that sum of left array is equal to sum of right array.

l = [1,2,3,1,1,1]

1 2 left side 1 rs => 6 3 left side 3 right side 3


# In[ ]:


# l = [1,2,1,1,5,1,4]
for index,value in enumerate(l[1:]):

    if sum(l[:index]) == sum(l[index + 1:]):
        
        print("eqi element is present at index {} and value is {}".format(index,l[index]))
        break


# # 3.Given 3 strings: first, second, and third.Third String is said to be a shuffle of first and second if it can be formed by interleaving the characters of first and second String in a way that maintains the left to right ordering of the characters from each string.
# 
# For example, given first = "abc" and second = "def", third = "dabecf" is a valid shuffle since it preserves the character ordering of the two strings. So, given these 3 strings write a program that detects whether the third String is a valid shuffle of first and second String.

# In[8]:


s1 = "abc"
s2 = "def"

s3 = "edabfc"

# 1 Iterate over s3 
# 2. Check if char is present in S1 or S2 
# 3. s1_pointer = 1 s2_pointer = 1 
s1_pointer = s2_pointer = 0
s3_index = 0
while s3_index < len(s3):
    
    if s3[s3_index] in s1 and s1[s1_pointer] == s3[s3_index]:
        s1_pointer+=1      
        
    elif s3[s3_index] in s2 and s2[s2_pointer] == s3[s3_index]:
         s2_pointer+=1
    else:
        print("Not a valid shuffle")
        break
    s3_index+=1
else:
    print("Valid shuffle")


# 4.A Program to check if strings are rotations of each other or not Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1 (eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
# 
# 5.Write a program to find all pairs in a list of Integers Whose sum is equal to a given Number.
# 
# For example nums = [1,2,3,4,5] sum = 7 expected output is ans = [(3,4),(2,5),(4,3),(5,2)]
# 
# 6.Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
# 
# For example if string is : "welcome" and shift is 4 the output will be "aipgtqi"
# 
# 7.Write aprogram to check if two given strings are anagram of each other or not.
# 
# Anagram Strings : if two given strings are anagrams of Each other. Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation, and capitalization. Eg : Input : "Army" and "Mary" Output "Strings are anagrams of each other"
# 
# 8.Write a program to find the first non repeated character of a given String

# In[ ]:




