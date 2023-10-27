def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "fizzbuzz"
    if x % 3 == 0:
        return "fizz"
    if x % 5 == 0:
        return "buzz" 
    return x

print(fizz_buzz(8))