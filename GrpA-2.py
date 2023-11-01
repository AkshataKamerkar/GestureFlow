# Grp_A : Assignment 2 


'''

        Write a Python program to store marks scored in subject “Fundamental of Data Structure” by
        N students in the class. Write functions to compute following:
        a) The average score of class
        b) Highest score and lowest score of class
        c) Count of students who were absent for the test
        d) Display mark with highest frequency

'''

mrkList1 = []
mrkList = []

n = int(input("Enter the number of Students : "))

for i in range(n):
    mrks = input(f'Enter the marks of Student {i + 1} : ')
    mrkList1.append(mrks)

for i in mrkList1:
    if i != "":
        j = int(i)
        mrkList.append(j)

total = 0
mrk_max = mrkList[0]
mrk_min = mrkList[0]
absStud = len(mrkList1) - len(mrkList)
freq = {}
highFreq = 0
highFreqEle = 0

for mrks in mrkList:

    # For Average
    total += (mrks)

    # For min and max    
    if (mrks) > mrk_max:
        mrk_max = (mrks)
    if (mrks) < mrk_min:
        mrk_min = (mrks)

    # For highest frequency
    if freq.get(mrks) == None:  # If the element is nt present thn count = 1
        freq[mrks] = 1

    else:  # If the element is present thn it is incremented by 1
        freq[mrks] += 1

for i in freq:  # Here i indicates keys of the dictionary
    if i > highFreqEle:
        highFreqEle = i
        highFreq = freq[i]  # Here freq[i] indicates value of the key i

print(f'a. The average score of the class : {total / n}')
print(f'b. The Highest Score is {mrk_max} and the Lowest Score is {mrk_min}')
print(f'c. The no. of Absent Students : {absStud}')
print(f'd. Marks with Highest Frequency are {highFreqEle} and its Frequency is {highFreq} ')
