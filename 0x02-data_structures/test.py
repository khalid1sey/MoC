

# names = ["chala","demeke","bontu","bana"]
# zeros = [0] * 5

# matrix = [[90,12],[92,12]] #2d matrix
# print(names[0])
# print(names[1 + 1])
# print(names[2])
# #print(names[4]) # out of range because accessing a list that doesnt exist
# # print(names[0] * 5)
# print(names[::2]) # every second number
# print(zeros)


# numbers = list(range(10))

# print(numbers)
# print (numbers[::2])



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
print(letters)

#removing
letters.pop(0)
letters.remove("b")
del letters[0:1]
print(letters)

#searching item with index
print(letters.count("d")) #returns reopitation of occurences
if "d" in letters:
    print(letters.index("d"))