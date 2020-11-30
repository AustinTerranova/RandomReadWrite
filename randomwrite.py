import random;

newCalculation = True;
while newCalculation:
    
    
    while True:
        try: 
            #print("please enter a number greater than 0");
            #paintPrice = int(input("Enter the price per a gallon of paint: "));

            randomNums = int(input("how many random numbers do you want "));
            randomNumLow = int(input("What is the lowest the random number should be: "));
            randomNumHigh = int(input("What is the highest the random number should be: "));
            

            if randomNums <= 0 & randomNumLow <=0 & randomNumHigh:
                print("please enter a number greater than 0 for all options");
                continue;
            break;
        except (ValueError, TypeError):
            print("please enter a valid integer");


    f = open("randomnum.txt", "w")
    
    
    #random.randint(randomNumLow, randomNumHigh);
    for x in range (0, randomNums):
        ran = str(random.randint(randomNumLow, randomNumHigh))
        f.writelines("%s\n" % ran) 
        print("\n",ran);
     
    f.close()
    print("The numbers were written to randomnum.txt");


    #f = open("randomnum.txt", "w")
    #f.write("N")
    #f.close()

    #/Users/austinterranova/Desktop/untitled folderopen and read the file after the appending:
    #f = open("demofile2.txt", "r")
   #print(f.read())
   

    again = input("If you want to play again type y: ");
    if again != "y":
        newCalculation = False;






