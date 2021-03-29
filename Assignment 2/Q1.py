from pprint import pprint


file1 = 'Assignment 2/file1.txt'
file2 = 'Assignment 2/file2.txt'

#
# a) Write a function readFile(filename) that reads the text file with the given filename and returns a
# list of the lines of text in the file. 

def readFile(filename):
    with open(filename, 'r') as document:
        lines = document.read().splitlines()
    return lines

lines_file1 = readFile(file1)
lines_file2 = readFile(file2)

#
# b) Write a function getWordsFromLineList(list) that parse the list of the lines of text into words and
# returns a list of all words found. 

def getWordsFromLineList(lines):
    words = ''
    lines = ''.join(lines).lower()
    for s in lines:
        if s.isalpha() or s.isspace():
            words += s
        else:
            words += ' '
    return words.split()

words_file1 = getWordsFromLineList(lines_file1)
words_file2 = getWordsFromLineList(lines_file2)


#
# c) Write a function countFrequency(list) that computes the frequency of each word in the list and
# returns a list of tuples in the form: (word, frequency).

def countFrequency(words):
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return [(k, v) for k, v in frequencies.items()]

frequencies_file1 = countFrequency(words_file1)
frequencies_file2 = countFrequency(words_file2)

#
# d) Implement a function mergeSort(list, column, ascending=True) that takes a list of tuples already
# loaded and uses Merge Sort to sort the data by the given column in ascending or descending order.
# For example, considering the list of tuples of the form: (word, frequency)
#   a. mergeSort(lst, 0, True) will sort the list by words in alphabetical order.
#   b. mergeSort(lst, 1, False) will sort the list by frequency in descending order.

def mergeSort(lst, col, ascending=True):
    if len(lst) < 2:
        return lst
        
    middle = len(lst)//2

    left = mergeSort(lst[:middle], col, ascending)
    right = mergeSort(lst[middle:], col, ascending)
    
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if (left[i][col] < right[j][col] and ascending) or (left[i][col] > right[j][col] and not(ascending)):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# print/use any
msorted1 = mergeSort(frequencies_file1, 0)
msorted2 = mergeSort(frequencies_file1, 0, False)
msorted3 = mergeSort(frequencies_file1, 1)
msorted4 = mergeSort(frequencies_file1, 1, False)

msorted5 = mergeSort(frequencies_file2, 0)
msorted6 = mergeSort(frequencies_file2, 0, False)
msorted7 = mergeSort(frequencies_file2, 1)
msorted8 = mergeSort(frequencies_file2, 1, False)

#
# e) Implement a function quickSort(list, column, ascending=True) that takes a list of tuples and uses
# Quick Sort to sort the data by the given column in ascending or descending order. The pivot element
# can be randomly selected. 

from random import randint
def quickSort(lst, col, ascending=True):
    if len(lst) < 2:
        return lst
    else:
        r = len(lst)
        pivot = randint(0, r-1)

        if ascending:
            left = [lst[i] for i in range(r) if lst[i][col] <= lst[pivot][col] and i != pivot]
            right = [lst[i] for i in range(r) if lst[i][col] > lst[pivot][col] and i != pivot]
        else:
            left = [lst[i] for i in range(r) if lst[i][col] > lst[pivot][col] and i != pivot]
            right = [lst[i] for i in range(r) if lst[i][col] <= lst[pivot][col] and i != pivot]

        return quickSort(left, col, ascending) + [lst[pivot]] + quickSort(right, col, ascending)

#print/use any
qsorted1 = quickSort(frequencies_file1, 0)
qsorted2 = quickSort(frequencies_file1, 0, False)
qsorted3 = quickSort(frequencies_file1, 1)
qsorted4 = quickSort(frequencies_file1, 1, False)

qsorted5 = quickSort(frequencies_file2, 0)
qsorted6 = quickSort(frequencies_file2, 0, False)
qsorted7 = quickSort(frequencies_file2, 1)
qsorted8 = quickSort(frequencies_file2, 1, False)

print(msorted1)
print('\n')
print(qsorted1)