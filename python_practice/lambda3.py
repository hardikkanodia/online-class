Dictionaries = [{'make':'Nokia','model':216,'color':'Black'},
                {'make':'Mi Max','model':56,'color':'Gold'},
                {'make':'Samsung','model':7,'color':'Blue'}]
# print("Original List of Dictionaries:")
# print(Dictionaries)


Dictionaries.sort(key = lambda x:x['make'])
print("Sorting the list of tuple:")
for i in Dictionaries:
    print(i)
