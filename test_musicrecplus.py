'''
Created on Nov 13, 2017

@author: jschm
'''
import sys
file_name_input = "musicrecplus.txt"
file_name_output = "musicrecplus.txt"

diction = {'a': ['d', 'a'], 'b': 'b', 'd': 'd', 'c' : 'c'}

data = {"brian":["Zach","Beethoven","Brahms","Mozart"], "Aill": ["don't know", "don'tcare"]}

for key in data:
    name = "brian"
    matches = num_matches(data[key], data[name])

file_name_input = "musicrecplus.txt"
file_name_output = "musicrecplus.txt"

name = ""
data = {}

"""asks for name and inputs data in file to dictionary"""
name = input("Enter your name (put a $ symbol after your name if you wish your "
    + "preferences to remain private): ")
##put data into data
input_file = open(file_name_input, 'r')   # Open the file for reading.
for line in input_file:            # Get one line at a time.
    user, artists = line.split(':')
    artists = artists.split(',')
    for i in range(len(artists)):
        artists[i] = artists[i].strip()
    #if you want to print everything
    #print(user + ' : ' + str(artists))
    data[user] = artists
    user = user.strip()
input_file.close() # Important - do not forget to close the file

print(data)


def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def selection_sort(L):
    n = len(L)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        if i != min_index:
            swap(L, i, min_index)
    return L

def sort_alpha_order_dictionary(dct):
    #start with sorting each value in the keys
    for key in dct:
        selection_sort(dct[key])
    return dct

users = selection_sort(list(diction))
result = []
for x in users:
    result += [x, diction[x]]
print(result)

# Writing a file.
def write_file(filename):
    '''Open existing or new file named filename.
       Write FILE_CONTENT to it.'''
    #sorts preferences in alphabetical order
    artists = sort_alpha_order_dictionary(data)
    users = selection_sort(list(data))
    result = []
    for u in users:
        result += [u, artists[u]]
    output_file = open(filename, 'w')
    for i in range(len(result)):
        if i % 2 == 0:
            output_file.write(result[i])
        else:
            output_file.write(":")
            for x in result[i]:
                output_file.write(x + ",")
            output_file.write("\n")
    output_file.close()
    
write_file("musicrecplus.txt")