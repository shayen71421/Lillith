#indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]
credit_no= "1234-5678-9012-3456"
print(credit_no[0])#prints the character on 0th index
print(credit_no[0:4])#prints the charaters from 0 to 4 (0,1,2,3)
print(credit_no[5:9])#prints the characters from 5 to 9(5,6,7,8)
print(credit_no[5:])#prints every chatacter from 5
print(credit_no[-1])#prints the character from back
print(credit_no[::2])#step :which prints characters in intervals of 2