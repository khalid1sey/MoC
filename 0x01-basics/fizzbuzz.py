

def fizzbuzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "fizzbuzz"
    if input % 3 == 0 :
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input
    


print(fizzbuzz(4))