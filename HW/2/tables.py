import time #To use in the printing

table = 0 #Itterating the variable table

while table > 100 or table < 1: #Loop infinitely until a sensible number is entered
    table = int(input("Enter a times table >>>"))

number = int(input("Up to what number >>>")) #To what number the multiplications go up to 

for x in range(1,number + 1): #Up to number + 1 so it will go to the desired number
    print("{0} X {1} = {2}".format(x,table,table*x)) #Prints the number, the user's number it is multiplying by and the answer
    time.sleep(1) #Aesthetics

