



count = 0;
try:
    f = open("randomnum.txt", "r")
    print("list of random numbers in random.txt: ");

    for x in f:
        print(x)
        count += 1;
    print("random number count: ",count);
except IOError:
    print("There is no file named randomnum.txt");


  
