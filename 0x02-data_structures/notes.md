

list - Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.


    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.


list is - ordered
        - changeable
        - allow duplicates
        - can contain different data types
        - defined as typeof objects
syntax: listname = [item1, item2, item(n)]
    it can be numbers,letters,names etc
    example letter = ["a", "b"]
             matrix = [[1,0],[2,3]]
            zeros = [0] * 5 returns 5 time s the list

    list constructor(list()): itrates through numbers 
    example list(range(20)) -prints numers in range of 1 -> 19

    msg = list("Hello, World") - prints the string as individual caharcters and lists them

    len(msg) returns size of a list 

    to acess member msg[0], msg[2-1]


    list unpacking - clean way to assign list item to variables
    ex. numbers = [1,2,3,4]
        first,second.third = numbers

        first, *other = numbers  the items after first will get packed to others

    
**accessing list**
names = ["chala","demeke","bontu","bana"]
zeros = [0] * 5

matrix = [[90,12],[92,12]] #2d matrix
print(names[0])
print(names[1 + 1])
print(names[2])
#print(names[4]) # out of range because accessing a list that doesnt exist
 print(names[0] * 5)
print(names[::2]) # every second number
print(zeros)


numbers = list(range(10))

print(numbers)
print (numbers[::2])


**packing list**
n = [1,2,4,43,42]

first,second,th,fo,fi = n
print(n)
print(first)
print(fi)

inti, *red = n #except 1 all items are packed to red because of (*)
print(red)

#loopint over lists
letters = ["a", "b"]
for index, letter in enumerate(letters): #it itrates with tuple
    print(index, letter)   

#adding and removing lists
#adding
letters.append("d")
letters.insert(0, "-")
letters.extend(numbers)  - appends element from another iterable lists,tuples,set,dicionry
print(letters)

#removing
letters.pop(0) #if index not provided the last item will be removed
letters.remove("b") #removes specified item
del letters[0:1]    #can also removes list
print(letters)
letters.clear() #empities the list 

#cheking or searching item with index
print(letters.count("d")) #returns reopitation of occurences
if "d" in letters:
    print(letters.index("d"))

#sorting
numbers = [3,2,5,2,43,5]

print(sorted(numbers, reverse=True))

print(numbers.sort(reverse=True))

#custom sort
items = [
    ("product" , 10),
    ("product" , 9),
    ("product" , 12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item item:item[1]) #this is lambda function
print(items)

lambda is small annonymous function
 -A lambda function can take any number of arguments, but can only have one expression.
  - syntax: lambda arguments : expression

items = [
    ("product" , 9),
    ("product" , 12),
    ("product" , 10),
]

def sort_item(item):
    return item[1]

#lambda function
items.sort(key=lambda item:item[1]) #this is lambda function
print(items)

sum = lambda a, b: a + b
print(sum(40,20))
func name = lambda arguments: expression
