

list - defines sequence of objects
    it can be numbers,letters,names etc
    example letter = ["a", "b"]
             matrix = [[1,0],[2,3]]
            zeros = [0] * 5 returns 5 time s the list

    list function(list()): itrates through numbers 
    example list(range(20)) -prints numers in range of 1 -> 19

    msg = list("Hello, World") - prints the string as individual caharcters and lists them

    len(msg) returns size of a list 

    to acess member msg[0], msg[2-1]


    list unpacking - clean way to assign list item to variables
    ex. numbers = [1,2,3,4]
        first,second.third = numbers

        first, *other = numbers  the items after first will get packed to others