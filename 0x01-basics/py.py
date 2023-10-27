
#------------string properties
# string1 = "String template"
# print(len(string1))
# print("sixth string is: " + string1[5])
# print("reverse of fifth string is: " + string1[-5]) #returns reverse position of strings character
# print("from first index to third index : " + string1[0:3]) #returns the characters from  rom first to fourth characters
# print("from first index up to fifth index : " + string1[:5])
# print("from the fifth index to last : " + string1[5: ])
# print(id(string1))
# print(id(string1[5]))

#--------------formatted string 
# fname = "khalid"
# lname = "santa"
# full = F"{fname} {lname}" #can be capital or small (f,F)
# print(full)
#------------string anotation
# age :int = 20  #the part :int is type anotation that discribes what data type we are refering bu its not necessary
# print(id(age))
# print(id(age))
# print(age)

#-------------for loop
# for i in range(20):
#     print(i)

# i = input()
# for x in i:
#     print(x)

# names = ["John", "Mary"]
# found = False
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         found = True
#         break
# else:
#     print("Not found")

#-------------ehile loop
# guess = 0
# answer = 5
# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass


#---------function
# def increement(number :int, by : int):
#     return (number + by)

# print(increement(number=21,by=3))

#--------------arguments(xargs)
# def multiply(*list): #the parameter becomes tuple because of asterisk
#     total = 1
#     for number in list:
#         total *= number
#     return total

# print(multiply(2,3,4,5))

#----------------------(xxargs)
# def save_user(**user):
#     print(user)

# save_user(id=1, name="admin")


#------debugging
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")